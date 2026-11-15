---

## 🔬 Dataset Engineering & Statistical Audit

Models were trained and validated on `marslanarshad/peach-tree-disease` (**4,301 field-captured images** featuring variable illumination, complex backgrounds, and multi-angle canopy shots)[cite: 11].

| Target Class | Biological Agent / Syndrome | Field Symptomatology & Agronomic Impact | Train (80%) | Valid (20%) | Share |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **`Anarsia lineatella`** | *Peach Twig Borer* (Insect) | Larvae tunnel into young terminal shoots causing wilting and perforate fruits[cite: 10]. | 294[cite: 11] | 74[cite: 11] | **8.56%**[cite: 11] |
| **`Grapholita molesta`** | *Oriental Fruit Moth* (Insect) | Attacks spring twigs before boring into fruit flesh near the stem[cite: 10]. | 241[cite: 11] | 61[cite: 11] | **7.02%**[cite: 11] |
| **`Dead Trees`** | *Systemic Dieback / Apoplexy* | Advanced decay or root asphyxiation requiring immediate orchard extraction[cite: 10]. | 49[cite: 11] | 13[cite: 11] | **1.44%**[cite: 11] |
| **`Healthy`** | *Vigorous Canopy* (Baseline) | Stress-free foliage serving as the healthy control reference[cite: 10]. | 2,855[cite: 11] | 714[cite: 11] | **82.98%**[cite: 11] |
| **TOTAL** | — | **Strictly aligned split via `random.seed(42)`**[cite: 11, 12] | **3,439**[cite: 11] | **862**[cite: 11] | **100%**[cite: 11] |

> **⚠️ Critical Data Insight (Severe Class Imbalance):** With `Healthy` accounting for **82.98%** of samples and `Dead Trees` representing just **1.44%** (49 training images), the dataset presents an extreme skew[cite: 11]. Overcoming majority-class bias without overfitting is a key test of architectural generalization[cite: 11].

---

## 📊 Experimental Benchmark: YOLOv11 vs. YOLO26

Both models were trained under identical conditions (`imgsz=224`, `batch=32`, `epochs=10`, Early Stopping `patience=5`) to isolate architectural efficiency[cite: 13, 14]:

| Evaluation Metric | YOLOv11 | YOLO26 | Engineering Delta |
| :--- | :---: | :---: | :--- |
| **Top-1 Validation Accuracy** | **83.0%**[cite: 15] | 81.1%[cite: 15] | `-1.9%` (Negligible trade-off)[cite: 15] |
| **Final Validation Loss** | **0.60**[cite: 15] | 0.63[cite: 15] | Equivalent convergence stability[cite: 15] |
| **Inference Latency / Image** | ~3.1 ms[cite: 15] | **~2.0 ms**[cite: 15] | ⚡ **35.5% Faster** (~500 FPS theoretical)[cite: 15] |
| **Exported Model Weight (`.pt`)** | ~5.2 MB[cite: 15] | **~3.1 MB**[cite: 15] | 💾 **40.4% Lighter** (Fits on-chip Flash)[cite: 15] |

### 🏆 Hardware Verdict: Why YOLO26 Dominates Edge Deployment
From an electrical and embedded systems engineering perspective, **YOLO26 is the clear winner** for real-world agricultural deployment[cite: 15]:
1. **On-Chip Memory Viability (-40.4% Footprint):** At **3.1 MB**, YOLO26 fits directly inside the internal Flash/SRAM of modern microcontrollers (**STM32H7, ESP32-S3, Raspberry Pi Zero**), eliminating external memory chips and simplifying Over-The-Air (OTA) firmware updates[cite: 15].
2. **Zero-Latency Drone Scanning (-35.5% Inference Time):** Processing a frame in **2.0 ms** prevents motion-blur bottlenecks during high-speed UAV orchard flyovers[cite: 15].
3. **Power Budget Preservation:** Fewer MAC (Multiply-Accumulate) operations per inference directly translate into extended battery autonomy on solar-assisted field sensor nodes[cite: 15].

---

## 🎥 Live Inference Demonstrations


https://github.com/user-attachments/assets/aed822ca-2750-40f5-b3f9-51f46978ab1e


https://github.com/user-attachments/assets/c6b7ec80-092b-46d4-842d-71c25582a0b7





* **YOLOv11 Inference Stream:** High-confidence real-time classification across pest and healthy foliage classes.
* **YOLO26 Inference Stream:** Ultra-fast edge-ready predictions demonstrating sub-2ms inference stability.

---

## 📂 Repository Structure

```text
peach-disease-detection-yolo/
├── src/
│   ├── train_yolov11.py               # Reproducible YOLOv11 training & ONNX export pipeline
│   └── train_yolo26.py                # Reproducible YOLO26 edge-optimized pipeline
├── notebooks/
│   ├── yolo11.mp4                     # YOLOv11 live inference recording
│   └── Yolo26.mp4                     # YOLO26 live inference recording
├── docs/
│   └── Rapport_IA_YOLO26_vs_YOLOv11.pdf  # Complete technical study & loss/accuracy curves
└── README.md
