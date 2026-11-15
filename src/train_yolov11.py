"""
Peach Tree Disease Classification - YOLOv11 Pipeline
Dataset: marslanarshad/peach-tree-disease (Kaggle)
Classes: Anarsia lineatella, Grapholita molesta, Dead Trees, Healthy
"""

import os
import random
import shutil
from ultralytics import YOLO


def prepare_dataset(src_dir="peach_dataset/peach_tree_disease/peach_tree_disease", output_dir="peach_yolo", seed=42):
    """Splits the dataset into 80% train and 20% validation sets with a fixed random seed."""
    classes = ["Anarsia lineatella", "Grapholita molesta", "Dead Trees", "Healthy"]
    random.seed(seed)

    total_train, total_valid = 0, 0
    for cls in classes:
        cls_path = os.path.join(src_dir, cls)
        if not os.path.exists(cls_path):
            raise FileNotFoundError(f"Directory not found: {cls_path}")

        imgs = [
            f for f in os.listdir(cls_path)
            if f.lower().endswith((".jpg", ".png", ".jpeg"))
        ]
        random.shuffle(imgs)
        split = int(0.8 * len(imgs))

        for subset, subset_imgs in [("train", imgs[:split]), ("valid", imgs[split:])]:
            dst = os.path.join(output_dir, subset, cls)
            os.makedirs(dst, exist_ok=True)
            for img in subset_imgs:
                shutil.copy(os.path.join(cls_path, img), dst)

        total_train += len(imgs[:split])
        total_valid += len(imgs[split:])
        print(f"{cls:<25} | Train: {len(imgs[:split]):>4} | Valid: {len(imgs[split:]):>4}")

    print("-" * 50)
    print(f"TOTAL: {total_train} train | {total_valid} valid ({total_train + total_valid} images)")
    return output_dir


def main():
    # 1. Prepare dataset (assumes Kaggle dataset is already downloaded and unzipped)
    dataset_path = prepare_dataset()

    # 2. Load pretrained YOLOv11 classification model
    model = YOLO("yolo11n-cls.pt")

    # 3. Train model with experimental hyperparameters
    model.train(
        data=dataset_path,
        imgsz=224,
        epochs=10,
        batch=32,
        patience=5,
        seed=42,
        project="runs/classify",
        name="yolov11_peach"
    )

    # 4. Validate and export model
    metrics = model.val()
    print(f"Top-1 Validation Accuracy: {metrics.top1:.4f}")
    model.export(format="onnx")


if __name__ == "__main__":
    main()
