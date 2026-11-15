<div align="center">

# Edge-AI Peach Orchard Diagnostics: YOLO26 vs. YOLOv11
### *Autonomous Phytosanitary Computer Vision Optimized for Resource-Constrained Embedded Systems*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLO26%20%7C%20YOLOv11-00FFFF?style=for-the-badge&logo=yolo&logoColor=black)](https://docs.ultralytics.com/)
[![GPU](https://img.shields.io/badge/Accelerator-NVIDIA%20T4%20(16GB)-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://colab.research.google.com/)
[![Edge AI](https://img.shields.io/badge/Target-STM32%20%7C%20ESP32%20%7C%20UAVs-FF6F00?style=for-the-badge&logo=espressif&logoColor=white)]()

**Author:** **Imen Rojbani** — *Electrical Engineering Student (ENSIT)*  
*Focus: Embedded Systems, Edge AI & Precision Agriculture*

</div>

---

## Engineering Vision & Problem Statement

In commercial peach (*Prunus persica*) orchards, biotic stresses—ranging from boring lepidopteran larvae to systemic vascular dieback—can devastate yields before human scouting detects macroscopic symptoms. Traditional manual inspection faces three structural bottlenecks: **diagnostic latency**, **observer subjectivity**, and **zero scalability** across industrial acreage.

> **Core Engineering Question:** *How can we design an autonomous vision pipeline capable of phytosanitary classification while shrinking its memory and compute footprint enough for INT8 deployment on battery-powered microcontrollers (STM32/ESP32) and high-speed agricultural drones?*

This repository presents a controlled benchmark between two Ultralytics nano-classification architectures—**YOLOv11n-cls** and **YOLO26n-cls**—evaluating accuracy alongside **model footprint, inference throughput, and edge-quantization readiness**.

---

## End-to-End Pipeline Architecture

```text
┌─────────────────────────┐      ┌──────────────────────────┐      ┌─────────────────────────┐
│    Kaggle Dataset API   │      │  Deterministic Splitter  │      │   GPU Training Engine   │
│   4,301 Orchard Images  │─────▶│  80% Train / 20% Valid   │─────▶│   NVIDIA T4 (16GB VRAM) │
│   (Uncontrolled Field)  │      │      Fixed Seed (42)     │      │   224x224 | Batch 32    │
└─────────────────────────┘      └──────────────────────────┘      └────────────┬────────────┘
                                                                                │
┌─────────────────────────┐      ┌──────────────────────────┐                   │
│     Edge Deployment     │      │  Comparative Benchmark   │                   │
│  • Drone Real-Time Feed │◀─────│  • Top-1 Val Accuracy    │◀──────────────────┘
│  • INT8 MCU Target (<1MB)│      │  • T4 Latency (ms/img)   │
│  • Low-Power Autonomy   │      │  • Binary Footprint (MB) │
└─────────────────────────┘      └──────────────────────────┘

```
| **`Anarsia lineatella`** | *Peach Twig Borer* (Insect) | Larvae tunnel into young terminal shoots causing wilting and perforate fruits. | 294 | 74 | **8.56%** |
| **`Grapholita molesta`** | *Oriental Fruit Moth* (Insect) | Attacks spring twigs before boring into fruit flesh near the stem. | 241 | 61 | **7.02%** |
| **`Dead Trees`** | *Systemic Dieback / Apoplexy* | Advanced decay or root asphyxiation requiring immediate orchard extraction. | 49 | 13 | **1.44%** |
| **`Healthy`** | *Vigorous Canopy* (Baseline) | Stress-free foliage serving as the healthy control reference. | 2,855 | 714 | **82.98%** |
| **TOTAL** | — | **Strictly aligned split via `random.seed(42)`** | **3,439** | **862** | **100%** |

> **Critical Data Insight (Severe Class Imbalance):** With `Healthy` accounting for **82.98%** of samples and `Dead Trees` representing just **1.44%** (49 training images), a naive majority-class baseline already yields **82.98%** Top-1 accuracy. Because Top-1 accuracy alone masks minority-class recall, future iterations will incorporate **class-weighted / focal loss**, **targeted oversampling**, and **per-class Macro-F1 tracking** to harden rare-disease sensitivity.

---

## Experimental Benchmark: YOLOv11n-cls vs. YOLO26n-cls

Both models were trained under identical hyperparameters (`imgsz=224`, `batch=32`, `epochs=10`, Early Stopping `patience=5`) on an **NVIDIA T4 GPU** to isolate architectural efficiency:

| Evaluation Metric | YOLOv11n-cls | YOLO26n-cls | Engineering Delta |
| :--- | :---: | :---: | :--- |
| **Top-1 Validation Accuracy** | **83.0%** | 81.1% | `-1.9%` (Within imbalance margin) |
| **Final Validation Loss** | **0.60** | 0.63 | Equivalent convergence stability |
| **Inference Latency (T4 GPU)** | ~3.1 ms | **~2.0 ms** | **35.5% Faster** (~500 FPS ceiling) |
| **Exported FP32 Weight (`.pt`)** | ~5.2 MB | **~3.1 MB** | **40.4% Lighter** (~0.8 MB post-INT8) |

### Hardware Verdict: Why YOLO26 Dominates Edge Deployment
From an electrical and embedded systems engineering perspective, **YOLO26n-cls is the superior candidate** for real-world agricultural deployment:
1. **MCU Flash/SRAM Viability (-40.4% Footprint):** At **3.1 MB (FP32)**, post-training **INT8 quantization** (via ONNX / TFLite Micro / STM32Cube.AI) compresses YOLO26 below **~0.9 MB**—allowing it to reside directly in the internal Flash/SRAM of **STM32H7** and **ESP32-S3** microcontrollers without external PSRAM overhead.
2. **High-Speed Drone Throughput (-35.5% Inference Time):** Cutting per-frame compute time by over a third provides vital headroom for CPU-bound edge SoCs (**Raspberry Pi Zero / Orange Pi**) and reduces motion-blur exposure constraints during UAV orchard flyovers.
3. **Power Budget Preservation:** Lower parameter count and fewer Multiply-Accumulate (MAC) operations per forward pass directly reduce dynamic switching energy ($E \propto C V^2 f$), extending battery autonomy on solar-assisted field nodes.

---

## Live Inference Demonstrations

### 1. YOLOv11 Real-Time Inference Stream


https://github.com/user-attachments/assets/642301ee-ebbf-49cf-9ea5-5bd93090148b


### 2. YOLO26 Ultra-Fast Edge Inference Stream



https://github.com/user-attachments/assets/7ca43486-2db0-4964-b02a-46c51e088f4f



---

## Repository Structure

```text
peach-disease-detection-yolo/
├── src/
│   ├── train_yolov11.py                  # Reproducible YOLOv11 training & ONNX export pipeline
│   └── train_yolo26.py                   # Reproducible YOLO26 edge-optimized pipeline
├── notebooks/
│   ├── yolo11.mp4                        # YOLOv11 live inference recording
│   └── Yolo26.mp4                        # YOLO26 live inference recording
├── docs/
│   └── Rapport_IA_YOLO26_vs_YOLOv11.pdf  # Complete technical study & loss/accuracy curves
└── README.md
