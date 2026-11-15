<div align="center">

# 🍑 Edge-AI Peach Orchard Diagnostics: YOLO26 vs. YOLOv11
### *Autonomous Phytosanitary Computer Vision Optimized for Resource-Constrained Embedded Systems*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLO26%20%7C%20YOLOv11-00FFFF?style=for-the-badge&logo=yolo&logoColor=black)](https://docs.ultralytics.com/)
[![GPU](https://img.shields.io/badge/Accelerator-NVIDIA%20T4%20(16GB)-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://colab.research.google.com/)
[![Edge AI](https://img.shields.io/badge/Target-STM32%20%7C%20ESP32%20%7C%20UAVs-FF6F00?style=for-the-badge&logo=espressif&logoColor=white)]()

**Author:** **Imen Rojbani** — *Electrical Engineering Student (ENSIT)*  
*Focus: Embedded Systems, Edge AI & Precision Agriculture*

</div>

---

## 🧠 Engineering Vision & Problem Statement

In commercial peach (*Prunus persica*) orchards, biotic stresses—ranging from boring lepidopteran larvae to systemic vascular dieback—can devastate yields before human scouting detects macroscopic symptoms. Traditional manual inspection faces three structural bottlenecks: **diagnostic latency**, **observer subjectivity**, and **zero scalability** across industrial acreage.

> **Core Engineering Question:** *How can we design an autonomous vision pipeline capable of high-precision phytosanitary classification while shrinking its memory and latency footprint enough to run natively on battery-powered microcontrollers (STM32/ESP32) and high-speed agricultural drones?*

This repository presents a rigorous, iso-parameter benchmark between two state-of-the-art Ultralytics architectures—**YOLOv11** and **YOLO26**—evaluating not just raw accuracy, but **hardware deployability, SRAM/Flash footprint, and real-time throughput**.

---

## 🏗️ End-to-End Pipeline Architecture

```text
┌─────────────────────────┐      ┌──────────────────────────┐      ┌─────────────────────────┐
│   Kaggle Dataset API    │      │  Deterministic Splitter  │      │   GPU Training Engine   │
│  4,301 Orchard Images   │─────▶│  80% Train / 20% Valid   │─────▶│   NVIDIA T4 (16GB VRAM) │
│   (Uncontrolled Field)  │      │     Fixed Seed (42)      │      │   224×224 | Batch 32    │
└─────────────────────────┘      └──────────────────────────┘      └────────────┬────────────┘
                                                                                │
┌─────────────────────────┐      ┌──────────────────────────┐                   │
│   Edge Deployment       │      │   Comparative Benchmark  │                   │
│  • Drone Real-Time Feed │◀─────│  • Top-1 Val Accuracy    │◀──────────────────┘
│  • MCU Flash (< 3.5 MB) │      │  • Inference Latency (ms)│
│  • Low-Power Autonomy   │      │  • Binary Footprint (MB) │



---

## 🔬 Dataset Engineering & Statistical Audit

Models were trained and validated on `marslanarshad/peach-tree-disease` (**4,301 field-captured images** featuring variable illumination, complex backgrounds, and multi-angle canopy shots).

| Target Class | Biological Agent / Syndrome | Field Symptomatology & Agronomic Impact | Train (80%) | Valid (20%) | Share |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **`Anarsia lineatella`** | *Peach Twig Borer* (Insect) | Larvae tunnel into young terminal shoots causing wilting and perforate fruits. | 294 | 74 | **8.56%** |
| **`Grapholita molesta`** | *Oriental Fruit Moth* (Insect) | Attacks spring twigs before boring into fruit flesh near the stem. | 241 | 61 | **7.02%** |
| **`Dead Trees`** | *Systemic Dieback / Apoplexy* | Advanced decay or root asphyxiation requiring immediate orchard extraction. | 49 | 13 | **1.44%** |
| **`Healthy`** | *Vigorous Canopy* (Baseline) | Stress-free foliage serving as the healthy control reference. | 2,855 | 714 | **82.98%** |
| **TOTAL** | — | **Strictly aligned split via `random.seed(42)`** | **3,439** | **862** | **100%** |

> **⚠️ Critical Data Insight (Severe Class Imbalance):** With `Healthy` accounting for **82.98%** of samples and `Dead Trees` representing just **1.44%** (49 training images), the dataset presents an extreme skew. Overcoming majority-class bias without overfitting is a key test of architectural generalization.

---

## 📊 Experimental Benchmark: YOLOv11 vs. YOLO26

Both models were trained under identical conditions (`imgsz=224`, `batch=32`, `epochs=10`, Early Stopping `patience=5`) to isolate architectural efficiency:

| Evaluation Metric | YOLOv11 | YOLO26 | Engineering Delta |
| :--- | :---: | :---: | :--- |
| **Top-1 Validation Accuracy** | **83.0%** | 81.1% | `-1.9%` (Negligible trade-off) |
| **Final Validation Loss** | **0.60** | 0.63 | Equivalent convergence stability |
| **Inference Latency / Image** | ~3.1 ms | **~2.0 ms** | ⚡ **35.5% Faster** (~500 FPS theoretical) |
| **Exported Model Weight (`.pt`)** | ~5.2 MB | **~3.1 MB** | 💾 **40.4% Lighter** (Fits on-chip Flash) |

### 🏆 Hardware Verdict: Why YOLO26 Dominates Edge Deployment
From an electrical and embedded systems engineering perspective, **YOLO26 is the clear winner** for real-world agricultural deployment:
1. **On-Chip Memory Viability (-40.4% Footprint):** At **3.1 MB**, YOLO26 fits directly inside the internal Flash/SRAM of modern microcontrollers (**STM32H7, ESP32-S3, Raspberry Pi Zero**), eliminating external memory chips and simplifying Over-The-Air (OTA) firmware updates.
2. **Zero-Latency Drone Scanning (-35.5% Inference Time):** Processing a frame in **2.0 ms** prevents motion-blur bottlenecks during high-speed UAV orchard flyovers.
3. **Power Budget Preservation:** Fewer MAC (Multiply-Accumulate) operations per inference directly translate into extended battery autonomy on solar-assisted field sensor nodes.

---

## 🎥 Live Inference Demonstrations

### 1. YOLOv11 Real-Time Inference Stream


https://github.com/user-attachments/assets/0120991f-5039-4b69-8f88-f59c1e226fc8



### 2. YOLO26 Ultra-Fast Edge Inference Stream


https://github.com/user-attachments/assets/373cee1f-9226-48b4-8e9f-de906b2cbb57



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
└─────────────────────────┘      └──────────────────────────┘
