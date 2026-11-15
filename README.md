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

In commercial peach (*Prunus persica*) orchards, biotic stresses—ranging from boring lepidopteran larvae to systemic vascular dieback—can devastate yields before human scouting detects macroscopic symptoms[cite: 9]. Traditional manual inspection faces three structural bottlenecks: **diagnostic latency**, **observer subjectivity**, and **zero scalability** across industrial acreage[cite: 9].

> **Core Engineering Question:** *How can we design an autonomous vision pipeline capable of high-precision phytosanitary classification while shrinking its memory and latency footprint enough to run natively on battery-powered microcontrollers (STM32/ESP32) and high-speed agricultural drones[cite: 10, 15]?*

This repository presents a rigorous, iso-parameter benchmark between two state-of-the-art Ultralytics architectures—**YOLOv11** and **YOLO26**—evaluating not just raw accuracy, but **hardware deployability, SRAM/Flash footprint, and real-time throughput**[cite: 9, 15].

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
└─────────────────────────┘      └──────────────────────────┘
---

## 🎥 Live Inference Demonstrations


https://github.com/user-attachments/assets/59f59de2-20a7-4296-975a-73cbde269103



https://github.com/user-attachments/assets/a22a0df3-4d40-4c7f-9159-a3e432dab049

