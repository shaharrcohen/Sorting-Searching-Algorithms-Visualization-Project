# 🔢 Sorting Algorithms Visualizer — Algorithmic Design of Sorting & Searching

> **Interactive visualization of classic sorting algorithms implemented in Python with real-time graphics and sound effects.**  
> Developed as part of the *Algorithmic Design — Sorting & Searching* course, this project demonstrates the logic, efficiency, and comparison between various sorting algorithms.

---

## 🎓 Project Summary
| Category | Details |
|-----------|----------|
| 🏫 **Course** | Algorithmic Design — Sorting and Searching |
| 💻 **Language** | Python (with Pygame) |
| 🧩 **Focus** | Visualization and performance analysis of classic sorting algorithms |
| 🎵 **Enhancements** | Audio feedback using unique sounds per algorithm |
| 👩‍💻 **Author** | Shahar Cohen |

---

## 🧠 Algorithms Implemented
The project includes **7 sorting algorithms**, each with a distinct color scheme and sound effect:

| Algorithm | Description | Sound File |
|------------|--------------|-------------|
| 🫧 **Bubble Sort** | Repeatedly swaps adjacent elements if they are in the wrong order. | `Bubble.mp3` |
| 💠 **Insertion Sort** | Builds the sorted array one item at a time. | `insertion.mp3` |
| 🔹 **Selection Sort** | Selects the smallest element and moves it to its correct place. | `selection.mp3` |
| ⚡ **Quick Sort** | Divide-and-conquer approach using partitioning. | `quick.mp3` |
| 🔄 **Cocktail Shaker Sort** | Bidirectional version of Bubble Sort. | `shaker.mp3` |
| 🧱 **Heap Sort** | Builds a heap and repeatedly extracts the max/min element. | `heap.mp3` |
| 🧩 **Merge Sort** | Recursively splits and merges sorted sublists. | (silent or optional) |

---

## 🧩 Features
| Feature | Description |
|----------|-------------|
| 🎨 **Real-Time Visualization** | Each comparison and swap is animated on screen. |
| 🧮 **Multiple Algorithms** | Compare sorting speeds visually and algorithmically. |
| 🔊 **Sound Integration** | Each sorting algorithm has its own looping background sound. |
| 🖱️ **Mouse & Keyboard Modes** | Choose between interactive mouse control or keyboard shortcuts. |
| 📈 **Dynamic Array Size** | Increase/decrease list size using UI buttons or keyboard keys. |
| 🎛️ **Ascending/Descending Options** | Sort data in both directions for comparison. |
| 🧠 **Educational Design** | Built for learning algorithm behavior step-by-step. |

---

## ⚙️ How It Works
- Each sorting function (`bubble_sort`, `quick_sort`, `heap_sort`, etc.) is implemented as a **Python generator**,  
  yielding control back to the main loop for real-time updates.
- The program uses **Pygame** to display bars representing values and colors them as the algorithm runs.
- Sorting steps are **synchronized with sounds** for a more intuitive learning experience.

---

## 🧮 Complexity Summary

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
|------------|------------|--------------|--------------|------------------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Cocktail Shaker | O(n) | O(n²) | O(n²) | O(1) |

---

## 🕹️ Controls

### 🧭 Keyboard Mode
| Key | Action |
|-----|--------|
| **R** | Reset array |
| **SPACE** | Start sorting |
| **A / D** | Ascending / Descending |
| **+ / -** | Increase / decrease list size |
| **I / B / S / M / Q / X / H** | Choose sorting algorithm (Insertion, Bubble, Selection, Merge, Quick, Shaker, Heap) |

### 🖱️ Mouse Mode
- Click buttons on screen to:
  - Select sorting algorithm  
  - Switch between ascending/descending  
  - Reset or resize array  

---

## 🧩 Files Included

| File | Description |
|------|--------------|
| `visualizer.py` | Main program — logic, sorting implementations, visualization, and event handling. |
| `Bubble.mp3` | Bubble Sort background sound. |
| `insertion.mp3` | Insertion Sort background sound. |
| `selection.mp3` | Selection Sort background sound. |
| `quick.mp3` | Quick Sort background sound. |
| `shaker.mp3` | Cocktail Shaker Sort background sound. |
| `heap.mp3` | Heap Sort background sound. |

---

## 🧭 How to Run
```bash
python visualizer.py
