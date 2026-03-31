import tkinter as tk
from tkinter import scrolledtext, ttk
import random

import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class SortVisualizer:
    def __init__(self, data):
        self.data = data.copy()
        self.steps = []

    def bubble_sort(self):
        data = self.data.copy()
        n = len(data)
        for i in range(n):
            for j in range(n - i - 1):
                self.steps.append(
                    {
                        "data": data.copy(),
                        "colors": [
                            "#00f5d4"
                            if k == j or k == j + 1
                            else ("#06d6a0" if k >= n - i else "#ef476f")
                            for k in range(n)
                        ],
                        "text": f"冒泡排序: 比较下标 {j} 和 {j + 1} 的值 {data[j]} 与 {data[j + 1]}",
                        "indices": [j, j + 1],
                        "markers": [("j", j), ("j+1", j + 1)],
                    }
                )
                if data[j] > data[j + 1]:
                    left_val, right_val = data[j], data[j + 1]
                    data[j], data[j + 1] = data[j + 1], data[j]
                    self.steps.append(
                        {
                            "data": data.copy(),
                            "colors": [
                                "#00f5d4"
                                if k == j or k == j + 1
                                else ("#06d6a0" if k >= n - i else "#ef476f")
                                for k in range(n)
                            ],
                            "text": (
                                f"冒泡排序: 交换下标 {j} 和 {j + 1} "
                                f"(值 {left_val} 与 {right_val})"
                            ),
                            "indices": [j, j + 1],
                            "markers": [("j", j), ("j+1", j + 1)],
                        }
                    )
        return self.steps

    def selection_sort(self):
        data = self.data.copy()
        n = len(data)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.steps.append(
                    {
                        "data": data.copy(),
                        "colors": [
                            "#00f5d4"
                            if k == j or k == min_idx
                            else ("#06d6a0" if k < i else "#ef476f")
                            for k in range(n)
                        ],
                        "text": (
                            f"选择排序: 比较下标 {j} 和当前最小下标 {min_idx} "
                            f"(值 {data[j]} 与 {data[min_idx]})"
                        ),
                        "indices": [j, min_idx],
                        "markers": [("i", i), ("min", min_idx), ("j", j)],
                    }
                )
                if data[j] < data[min_idx]:
                    min_idx = j
                    self.steps.append(
                        {
                            "data": data.copy(),
                            "colors": [
                                "#ffd166" if k == min_idx else ("#06d6a0" if k < i else "#ef476f")
                                for k in range(n)
                            ],
                            "text": f"选择排序: 更新最小值下标为 {min_idx} (值 {data[min_idx]})",
                            "indices": [min_idx],
                            "markers": [("i", i), ("min", min_idx)],
                        }
                    )
            old_i_val, old_min_val = data[i], data[min_idx]
            data[i], data[min_idx] = data[min_idx], data[i]
            self.steps.append(
                {
                    "data": data.copy(),
                    "colors": ["#06d6a0" if k <= i else "#ef476f" for k in range(n)],
                    "text": (
                        f"选择排序: 交换下标 {i} 和 {min_idx} "
                        f"(值 {old_i_val} 与 {old_min_val})"
                    ),
                    "indices": [i, min_idx],
                    "markers": [("i", i), ("min", min_idx)],
                }
            )
        return self.steps

    def insertion_sort(self):
        data = self.data.copy()
        n = len(data)
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                self.steps.append(
                    {
                        "data": data.copy(),
                        "colors": [
                            "#00f5d4"
                            if k == j or k == j + 1
                            else ("#06d6a0" if k < i else "#ef476f")
                            for k in range(n)
                        ],
                        "text": f"插入排序: 将下标 {j} 的值 {data[j]} 右移到下标 {j + 1}",
                        "indices": [j, j + 1],
                        "markers": [("key", i), ("j", j), ("j+1", j + 1)],
                    }
                )
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
            self.steps.append(
                {
                    "data": data.copy(),
                    "colors": ["#06d6a0" if k <= i else "#ef476f" for k in range(n)],
                    "text": (
                        f"插入排序: 将原下标 {i} 的值 {key} "
                        f"插入到下标 {j + 1}"
                    ),
                    "indices": [i, j + 1],
                    "markers": [("key", i), ("pos", j + 1)],
                }
            )
        return self.steps

    def quick_sort(self):
        data = self.data.copy()
        self._quick_sort_helper(data, 0, len(data) - 1)
        return self.steps

    def _quick_sort_helper(self, data, low, high):
        if low < high:
            pi = self._partition(data, low, high)
            self._quick_sort_helper(data, low, pi - 1)
            self._quick_sort_helper(data, pi + 1, high)

    def _partition(self, data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            self.steps.append(
                {
                    "data": data.copy(),
                    "colors": [
                        "#00f5d4"
                        if k == j or k == high
                        else ("#06d6a0" if k <= i else "#ef476f")
                        for k in range(len(data))
                    ],
                    "text": (
                        f"快速排序: 比较下标 {j} 的值 {data[j]} "
                        f"与枢纽下标 {high} 的值 {pivot}"
                    ),
                    "indices": [j, high],
                    "markers": [("i", i), ("j", j), ("pivot", high)],
                }
            )
            if data[j] < pivot:
                i += 1
                if i != j:
                    left_val, right_val = data[i], data[j]
                    data[i], data[j] = data[j], data[i]
                    self.steps.append(
                        {
                            "data": data.copy(),
                            "colors": [
                                "#ffd166" if k == i or k == j else "#ef476f"
                                for k in range(len(data))
                            ],
                            "text": (
                                f"快速排序: 交换下标 {i} 和 {j} "
                                f"(值 {left_val} 与 {right_val})"
                            ),
                            "indices": [i, j],
                            "markers": [("i", i), ("j", j), ("pivot", high)],
                        }
                    )
                else:
                    data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        pivot_left_val, pivot_right_val = data[high], data[i + 1]
        self.steps.append(
            {
                "data": data.copy(),
                "colors": ["#06d6a0" if k == i + 1 else "#ef476f" for k in range(len(data))],
                "text": (
                    f"快速排序: 交换下标 {i + 1} 和 {high} "
                    f"(值 {pivot_right_val} 与 {pivot_left_val})，枢纽就位"
                ),
                "indices": [i + 1, high],
                "markers": [("pivot_new", i + 1), ("pivot_old", high)],
            }
        )
        return i + 1


class SortVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("排序算法可视化")
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        win_w = min(1280, int(screen_w * 0.9))
        win_h = min(820, int(screen_h * 0.9))
        pos_x = max(0, (screen_w - win_w) // 2)
        pos_y = max(0, (screen_h - win_h) // 2)
        self.root.geometry(f"{win_w}x{win_h}+{pos_x}+{pos_y}")
        self.root.minsize(980, 680)
        self.root.configure(bg="#1a1a2e")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Microsoft YaHei UI", 10))
        style.configure("TLabel", background="#1a1a2e", foreground="white")
        style.configure("TCombobox", font=("Microsoft YaHei UI", 10))

        control_frame = ttk.Frame(root)
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        ttk.Label(control_frame, text="选择算法:").pack(side=tk.LEFT, padx=5)
        self.algorithm_var = tk.StringVar(value="冒泡排序")
        algorithm_combo = ttk.Combobox(
            control_frame,
            textvariable=self.algorithm_var,
            values=["冒泡排序", "选择排序", "插入排序", "快速排序"],
            state="readonly",
            width=12,
        )
        algorithm_combo.pack(side=tk.LEFT, padx=5)
        algorithm_combo.bind("<<ComboboxSelected>>", self.on_algorithm_changed)

        ttk.Label(control_frame, text="速度:").pack(side=tk.LEFT, padx=5)
        self.speed_var = tk.IntVar(value=180)
        speed_scale = ttk.Scale(
            control_frame,
            from_=10,
            to=500,
            orient=tk.HORIZONTAL,
            variable=self.speed_var,
            length=150,
        )
        speed_scale.pack(side=tk.LEFT, padx=5)

        ttk.Label(control_frame, text="数据大小:").pack(side=tk.LEFT, padx=5)
        self.size_var = tk.IntVar(value=30)
        size_scale = ttk.Scale(
            control_frame,
            from_=5,
            to=100,
            orient=tk.HORIZONTAL,
            variable=self.size_var,
            length=150,
        )
        size_scale.pack(side=tk.LEFT, padx=5)

        ttk.Button(control_frame, text="开始", command=self.start_sort).pack(side=tk.LEFT, padx=5)
        self.pause_button = ttk.Button(
            control_frame, text="暂停", command=self.pause_sort, state=tk.DISABLED
        )
        self.pause_button.pack(side=tk.LEFT, padx=5)
        self.resume_button = ttk.Button(
            control_frame, text="恢复", command=self.resume_sort, state=tk.DISABLED
        )
        self.resume_button.pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="单步", command=self.step_sort).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="重置", command=self.reset).pack(side=tk.LEFT, padx=5)

        self.info_label = ttk.Label(root, text="准备就绪")
        self.info_label.pack(side=tk.TOP, padx=10, pady=5)

        content_frame = ttk.Panedwindow(root, orient=tk.HORIZONTAL)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.fig, self.ax = plt.subplots(figsize=(10, 5), facecolor="#1a1a2e")
        self.ax.set_facecolor("#252540")
        chart_frame = ttk.Frame(content_frame)
        self.canvas = FigureCanvasTkAgg(self.fig, master=chart_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        tutorial_frame = ttk.Frame(content_frame)
        table_frame = ttk.LabelFrame(tutorial_frame, text="数组状态表")
        table_frame.pack(fill=tk.X, pady=(0, 8))
        self.index_row_var = tk.StringVar(value="下标: -")
        self.value_row_var = tk.StringVar(value="数值: -")
        ttk.Label(
            table_frame,
            textvariable=self.index_row_var,
            font=("Consolas", 10),
            anchor=tk.W,
            justify=tk.LEFT,
        ).pack(fill=tk.X, padx=6, pady=(4, 2))
        ttk.Label(
            table_frame,
            textvariable=self.value_row_var,
            font=("Consolas", 10),
            anchor=tk.W,
            justify=tk.LEFT,
        ).pack(fill=tk.X, padx=6, pady=(0, 4))

        ttk.Label(tutorial_frame, text="过程讲解").pack(anchor=tk.W, pady=(0, 6))
        self.tutorial_text = scrolledtext.ScrolledText(
            tutorial_frame,
            width=36,
            height=18,
            wrap=tk.WORD,
            bg="#13132a",
            fg="white",
            insertbackground="white",
            font=("Microsoft YaHei UI", 10),
        )
        self.tutorial_text.pack(fill=tk.BOTH, expand=True)
        self.tutorial_text.configure(state=tk.DISABLED)
        content_frame.add(chart_frame, weight=3)
        content_frame.add(tutorial_frame, weight=2)

        self.data = []
        self.animator = None
        self.step_idx = 0
        self.steps = []
        self.bars = None
        self.is_paused = False
        self.steps_algorithm = None
        self.steps_size = None

        self._set_chinese_font()
        self.reset()

    def _set_chinese_font(self):
        plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Arial Unicode MS"]
        plt.rcParams["axes.unicode_minus"] = False

    def _build_steps(self):
        algorithm = self.algorithm_var.get()
        visualizer = SortVisualizer(self.data)
        if algorithm == "冒泡排序":
            return visualizer.bubble_sort()
        if algorithm == "选择排序":
            return visualizer.selection_sort()
        if algorithm == "插入排序":
            return visualizer.insertion_sort()
        return visualizer.quick_sort()

    def _prepare_teaching_session(self, regenerate_data):
        if regenerate_data:
            self.data = [random.randint(10, 100) for _ in range(self.size_var.get())]
        algorithm = self.algorithm_var.get()
        self.steps = self._build_steps()
        self.steps_algorithm = algorithm
        self.steps_size = len(self.data)
        self.step_idx = 0
        self.is_paused = False
        self.pause_button.config(state=tk.NORMAL)
        self.resume_button.config(state=tk.DISABLED)

        intro = self._algorithm_teaching_text(algorithm)
        separator = "=" * 28
        self._set_tutorial(
            f"{algorithm} 教学模式\n"
            f"{separator}\n"
            f"{intro}\n"
            f"{separator}\n"
            "开始演示:\n"
        )

    def _algorithm_teaching_text(self, algorithm):
        if algorithm == "冒泡排序":
            return (
                "算法思路:\n"
                "1. 每一轮从左到右比较相邻元素。\n"
                "2. 若左边大于右边，就交换。\n"
                "3. 每轮结束后，最大值会沉到末尾。\n"
                "时间复杂度: O(n^2)"
            )
        if algorithm == "选择排序":
            return (
                "算法思路:\n"
                "1. 在未排序区间中寻找最小值。\n"
                "2. 将最小值放到当前起始位置。\n"
                "3. 已排序区间不断向右扩大。\n"
                "时间复杂度: O(n^2)"
            )
        if algorithm == "插入排序":
            return (
                "算法思路:\n"
                "1. 默认第一个元素已排序。\n"
                "2. 取下一个元素，向左寻找插入位置。\n"
                "3. 比它大的元素右移，为它腾出位置。\n"
                "时间复杂度: O(n^2)"
            )
        return (
            "算法思路:\n"
            "1. 选择一个枢纽值，把数组划分为两部分。\n"
            "2. 左边都小于枢纽，右边都大于等于枢纽。\n"
            "3. 对左右两侧递归执行同样过程。\n"
            "平均时间复杂度: O(n log n)"
        )

    def _set_tutorial(self, text):
        self.tutorial_text.configure(state=tk.NORMAL)
        self.tutorial_text.delete("1.0", tk.END)
        self.tutorial_text.insert(tk.END, text)
        self.tutorial_text.configure(state=tk.DISABLED)

    def _append_tutorial(self, text):
        self.tutorial_text.configure(state=tk.NORMAL)
        self.tutorial_text.insert(tk.END, text + "\n")
        self.tutorial_text.see(tk.END)
        self.tutorial_text.configure(state=tk.DISABLED)

    def _update_array_table(self, values):
        idx_row = " ".join(f"{i:02d}" for i in range(len(values)))
        val_row = " ".join(f"{v:02d}" for v in values)
        self.index_row_var.set(f"下标: {idx_row}")
        self.value_row_var.set(f"数值: {val_row}")

    def _draw_value_labels(self, values):
        for idx, val in enumerate(values):
            self.ax.text(
                idx,
                val + 1,
                str(val),
                ha="center",
                va="bottom",
                color="white",
                fontsize=8,
            )

    def _mark_indices(self, values, markers):
        if not markers:
            return
        grouped = {}
        for name, idx in markers:
            if 0 <= idx < len(values):
                grouped.setdefault(idx, [])
                if name not in grouped[idx]:
                    grouped[idx].append(name)

        for idx, names in grouped.items():
            # 垂直堆叠标签：从上到下排列
            for i, name in enumerate(names):
                y_offset = values[idx] + 15 - i * 8  # min在上（15），i在下（7）
                self.ax.text(
                    idx,
                    y_offset,
                    f"{name}={idx}",
                    ha="center",
                    va="bottom",
                    color="#ffd166",
                    fontsize=9,
                    fontweight="bold",
                )

    def _indices_text(self, step):
        markers = step.get("markers", [])
        if markers:
            return "下标: " + ", ".join(f"{name}={idx}" for name, idx in markers)
        indices = step.get("indices", [])
        if not indices:
            return "下标: -"
        return "下标: " + ", ".join(str(i) for i in indices)

    def _render_step(self, step):
        self.ax.clear()
        self.bars = self.ax.bar(
            range(len(step["data"])), step["data"], color=step["colors"], width=0.8
        )
        self._draw_value_labels(step["data"])
        self._mark_indices(step["data"], step.get("markers", []))
        self.ax.set_ylim(0, 105)
        self.ax.set_title(self.algorithm_var.get(), color="white", fontsize=14)
        self.ax.set_xlabel("下标", color="white")
        self.ax.set_xticks(range(len(step["data"])))
        self.ax.set_xticklabels(range(len(step["data"])), color="white", fontsize=8)
        self.ax.tick_params(colors="white")
        self.info_label.config(
            text=(
                f"步数: {self.step_idx + 1}/{len(self.steps)} | "
                f"{step['text']} | {self._indices_text(step)}"
            )
        )
        self._update_array_table(step["data"])
        self._append_tutorial(
            f"第{self.step_idx + 1}步: {step['text']} | {self._indices_text(step)}"
        )

    def draw_initial(self):
        self.ax.clear()
        colors = ["#ef476f"] * len(self.data)
        self.bars = self.ax.bar(range(len(self.data)), self.data, color=colors, width=0.8)
        self._draw_value_labels(self.data)
        self.ax.set_ylim(0, 105)
        self.ax.set_title("准备排序", color="white", fontsize=14)
        self.ax.set_xlabel("下标", color="white")
        self.ax.set_xticks(range(len(self.data)))
        self.ax.set_xticklabels(range(len(self.data)), color="white", fontsize=8)
        self.ax.tick_params(colors="white")
        self._update_array_table(self.data)
        self.canvas.draw()

    def start_sort(self):
        self._prepare_teaching_session(regenerate_data=True)

        if self.animator:
            self.animator.event_source.stop()

        interval = 601 - self.speed_var.get()
        self.animator = animation.FuncAnimation(
            self.fig,
            self.update_frame,
            frames=len(self.steps),
            interval=interval,
            repeat=False,
        )
        self.canvas.draw()

    def update_frame(self, _frame):
        if self.is_paused:
            return self.bars
        if self.step_idx < len(self.steps):
            step = self.steps[self.step_idx]
            self._render_step(step)
            self.step_idx += 1
            self.canvas.draw_idle()
        return self.bars

    def pause_sort(self):
        self.is_paused = True
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.NORMAL)
        self.info_label.config(text=f"已暂停 - 步数: {self.step_idx}/{len(self.steps)}")

    def resume_sort(self):
        self.is_paused = False
        self.pause_button.config(state=tk.NORMAL)
        self.resume_button.config(state=tk.DISABLED)
        self.info_label.config(text=f"已恢复 - 步数: {self.step_idx}/{len(self.steps)}")

    def step_sort(self):
        need_rebuild = (
            (not self.steps)
            or self.steps_algorithm != self.algorithm_var.get()
            or self.steps_size != self.size_var.get()
            or self.step_idx >= len(self.steps)
        )

        if need_rebuild:
            self._prepare_teaching_session(regenerate_data=True)
            self.info_label.config(text="已进入单步教学模式")

        # 单步时强制暂停自动播放，避免与动画抢帧。
        self.is_paused = True
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.NORMAL)

        if self.step_idx < len(self.steps):
            step = self.steps[self.step_idx]
            self._render_step(step)
            self.canvas.draw()
            self.step_idx += 1

    def reset(self):
        if self.animator:
            self.animator.event_source.stop()
        self.data = [random.randint(10, 100) for _ in range(self.size_var.get())]
        self.step_idx = 0
        self.steps = []
        self.steps_algorithm = None
        self.steps_size = None
        self.is_paused = False
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.DISABLED)
        self.draw_initial()
        self.info_label.config(text="准备就绪")
        self._set_tutorial(
            "欢迎使用排序算法教学模式。\n"
            "点击开始后，右侧会实时记录每一步比较/交换过程。\n"
            "柱子上方数字表示当前元素值。"
        )

    def on_algorithm_changed(self, _event=None):
        # 算法切换后让旧步骤失效，避免单步沿用上次算法的过程。
        self.steps = []
        self.step_idx = 0
        self.steps_algorithm = None
        self.steps_size = None
        if self.animator:
            self.animator.event_source.stop()
        self.is_paused = False
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.DISABLED)
        self.info_label.config(text=f"已切换算法: {self.algorithm_var.get()}（可开始或单步）")


if __name__ == "__main__":
    root = tk.Tk()
    app = SortVisualizerApp(root)
    root.mainloop()
