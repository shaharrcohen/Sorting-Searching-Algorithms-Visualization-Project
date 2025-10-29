from os import environ
import pygame
import random
import math

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    SEA_GREEN = 159, 226, 191
    PINK_PASTEL = 248, 200, 220
    T_COLOR = 150, 121, 105
    LF_COLOR = 196, 164, 132
    SO_COLOR = 128, 0, 0
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    FONT = pygame.font.SysFont('Segoe script', 14)
    LARGE_FONT = pygame.font.SysFont('Lucida Handwriting', 16)
    TITLE_FONT = pygame.font.SysFont('Stencil', 36)

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def draw_buttons(draw_info, buttons):
    for button in buttons:
        pygame.draw.rect(draw_info.window, button['color'], button['rect'])
        text_surface = draw_info.FONT.render(button['text'], True, draw_info.BLACK)
        draw_info.window.blit(text_surface, (button['rect'].x + 5, button['rect'].y + 5))


def draw(draw_info, algo_name, ascending, buttons, show_controls=False):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.TITLE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1,
                                        draw_info.T_COLOR)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    if show_controls:
        controls = draw_info.LARGE_FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending | "
                                               "Size - + or - ", 1,
                                               draw_info.LF_COLOR)
        draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 45))

        sorting = draw_info.FONT.render(
            "I - Insertion | B - Bubble | S - Selection | M - Merge | Q - Quick | Shaker - X | Heap - H",
            1, draw_info.SO_COLOR)
        draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 75))

    draw_list(draw_info)
    draw_buttons(draw_info, buttons)
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()


def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.SEA_GREEN, j + 1: draw_info.PINK_PASTEL}, True)
                yield True
    return lst


def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(1, len(lst)):
        current = lst[i]
        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_list(draw_info, {i - 1: draw_info.SEA_GREEN, i: draw_info.PINK_PASTEL}, True)
            yield True
    return lst


def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    for i in range(n):
        swap_inx = i
        for j in range(i + 1, n):
            if (ascending and lst[j] < lst[swap_inx]) or (not ascending and lst[j] > lst[swap_inx]):
                swap_inx = j

        # Swap the elements
        lst[i], lst[swap_inx] = lst[swap_inx], lst[i]

        # Update the display to show the current sorting state
        draw_list(draw_info, {i: draw_info.SEA_GREEN, swap_inx: draw_info.PINK_PASTEL}, True)
        yield True
    return lst


# Implementing Merge sort by 2 functions - merge&merge sort
def merge(draw_info, left, mid, right, ascending=True):
    lst = draw_info.lst
    left_copy = lst[left: mid + 1]
    right_copy = lst[mid + 1: right + 1]
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if (left_copy[left_copy_index] < right_copy[right_copy_index] and ascending) or (
                left_copy[left_copy_index] >= right_copy[right_copy_index] and not ascending):
            lst[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        else:
            lst[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1

        draw_list(draw_info, {sorted_index: draw_info.SEA_GREEN}, True)
        sorted_index += 1
        yield True

    while left_copy_index < len(left_copy):
        lst[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1
        draw_list(draw_info, {sorted_index: draw_info.PINK_PASTEL}, True)
        yield True

    while right_copy_index < len(right_copy):
        lst[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1
        draw_list(draw_info, {sorted_index: draw_info.SEA_GREEN}, True)
        yield True


def merge_sort(draw_info, left, right, ascending=True):
    lst = draw_info.lst
    if left >= right:
        return
    mid = (left + right) // 2
    yield from merge_sort(draw_info, left, mid, ascending)
    yield from merge_sort(draw_info, mid + 1, right, ascending)
    yield from merge(draw_info, left, mid, right, ascending)


def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst

    def partition(low, high):
        pivot = lst[high]
        i = low - 1
        for j in range(low, high):
            if (lst[j] < pivot and ascending) or (lst[j] > pivot and not ascending):
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
                draw_list(draw_info, {i: draw_info.SEA_GREEN, j: draw_info.PINK_PASTEL}, True)
                yield True
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        draw_list(draw_info, {i + 1: draw_info.SEA_GREEN, high: draw_info.PINK_PASTEL}, True)
        yield True
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = yield from partition(low, high)
            yield from quick_sort_recursive(low, pi - 1)
            yield from quick_sort_recursive(pi + 1, high)

    yield from quick_sort_recursive(0, len(lst) - 1)
    return lst


def cocktail_shaker_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False
        for i in range(start, end):
            if (ascending and lst[i] > lst[i + 1]) or (not ascending and lst[i] < lst[i + 1]):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
                draw_list(draw_info, {i: draw_info.SEA_GREEN, i + 1: draw_info.PINK_PASTEL}, True)
                yield True

        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if (ascending and lst[i] > lst[i + 1]) or (not ascending and lst[i] < lst[i + 1]):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
                draw_list(draw_info, {i: draw_info.SEA_GREEN, i + 1: draw_info.PINK_PASTEL}, True)
                yield True

        start = start + 1


def heapify(draw_info, n, i, ascending=True):
    lst = draw_info.lst
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and ((lst[i] < lst[l] and ascending) or (lst[i] > lst[l] and not ascending)):
        largest = l

    if r < n and ((lst[largest] < lst[r] and ascending) or (lst[largest] > lst[r] and not ascending)):
        largest = r

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        draw_list(draw_info, {i: draw_info.SEA_GREEN, largest: draw_info.PINK_PASTEL}, True)
        yield True
        yield from heapify(draw_info, n, largest, ascending)


def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(draw_info, n, i, ascending)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        draw_list(draw_info, {i: draw_info.SEA_GREEN, 0: draw_info.PINK_PASTEL}, True)
        yield from heapify(draw_info, i, 0, ascending)


# function which creates a selection tool window.
def draw_initial_selection_screen(window, width, height, buttons):
    window.fill(DrawInformation.BACKGROUND_COLOR)

    title_font = pygame.font.SysFont('Stencil', 36)
    button_font = pygame.font.SysFont('Lucida Handwriting', 24)

    title = title_font.render("Select Input Method", True, DrawInformation.T_COLOR)
    window.blit(title, (width // 2 - title.get_width() // 2, height // 4 - title.get_height() // 2))

    for button in buttons:
        pygame.draw.rect(window, DrawInformation.LF_COLOR, button['rect'])
        text_surf = button_font.render(button['text'], True, DrawInformation.BLACK)
        text_rect = text_surf.get_rect(center=button['rect'].center)
        window.blit(text_surf, text_rect)

    pygame.display.update()

# Adding sounds for each sort
def play_sorting_sound(algo_name):
    sound_files = {
        "Bubble Sort": "Bubble.mp3",
        "Insertion Sort": "insertion.mp3",
        "Selection Sort": "selection.mp3",
        "Quick Sort": "quick.mp3",
        "Cocktail Shaker Sort": "shaker.mp3",
        "Heap Sort": "heap.mp3"
    }
    if algo_name in sound_files:
        try:
            print(f"Loading sound: {sound_files[algo_name]} for {algo_name}")
            pygame.mixer.music.load(sound_files[algo_name])
            pygame.mixer.music.play(-1)
            return True
        except pygame.error as e:
            print(f"Error loading sound file '{sound_files[algo_name]}': {e}")
            return False
    return False


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50  # Initial size of the array
    min_val = 0
    max_val = 100
    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)

    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None
    sound_enabled = False
    # Selection window qualities
    window = draw_info.window
    buttons = [
        {'text': 'Keyboard', 'rect': pygame.Rect(300, 300, 200, 50)},
        {'text': 'Mouse', 'rect': pygame.Rect(300, 400, 200, 50)}
    ]
    input_method = None
    # Defining the mouse window.
    mouse_buttons = [
        {'rect': pygame.Rect(10, 60, 120, 30), 'text': "Bubble Sort", 'color': draw_info.LF_COLOR,
         'action': 'bubble_sort'},
        {'rect': pygame.Rect(140, 60, 120, 30), 'text': "Insertion Sort", 'color': draw_info.LF_COLOR,
         'action': 'insertion_sort'},
        {'rect': pygame.Rect(270, 60, 120, 30), 'text': "Selection Sort", 'color': draw_info.LF_COLOR,
         'action': 'selection_sort'},
        {'rect': pygame.Rect(400, 60, 120, 30), 'text': "Merge Sort", 'color': draw_info.LF_COLOR,
         'action': 'merge_sort'},
        {'rect': pygame.Rect(530, 60, 120, 30), 'text': "Quick Sort", 'color': draw_info.LF_COLOR,
         'action': 'quick_sort'},
        {'rect': pygame.Rect(660, 60, 120, 30), 'text': "Shaker Sort", 'color': draw_info.LF_COLOR,
         'action': 'cocktail_shaker_sort'},
        {'rect': pygame.Rect(10, 100, 120, 30), 'text': "Heap Sort", 'color': draw_info.LF_COLOR,
         'action': 'heap_sort'},
        {'rect': pygame.Rect(140, 100, 120, 30), 'text': "Ascending", 'color': draw_info.LF_COLOR,
         'action': 'ascending'},
        {'rect': pygame.Rect(270, 100, 120, 30), 'text': "Descending", 'color': draw_info.LF_COLOR,
         'action': 'descending'},
        {'rect': pygame.Rect(400, 100, 120, 30), 'text': "New List", 'color': draw_info.LF_COLOR, 'action': 'new_list'},
        {'rect': pygame.Rect(530, 100, 120, 30), 'text': "+ Size", 'color': draw_info.LF_COLOR,
         'action': 'increase_size'},
        {'rect': pygame.Rect(660, 100, 120, 30), 'text': "- Size", 'color': draw_info.LF_COLOR,
         'action': 'decrease_size'},
    ]

    while run:
        clock.tick(60)

        if input_method is None:
            draw_initial_selection_screen(window, draw_info.width, draw_info.height, buttons)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button in buttons:
                        if button['rect'].collidepoint(mouse_pos):
                            input_method = button['text']

            continue

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
                if sound_enabled:
                    pygame.mixer.music.stop()
                    sound_enabled = False
        else:
            if input_method == 'Keyboard':
                draw(draw_info, sorting_algo_name, ascending, [], show_controls=True)
            else:
                draw(draw_info, sorting_algo_name, ascending, mouse_buttons)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if input_method == 'Keyboard':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        lst = generate_starting_list(n, min_val, max_val)
                        draw_info.set_list(lst)
                        sorting = False
                        if sound_enabled:
                            pygame.mixer.music.stop()
                            sound_enabled = False
                    elif event.key == pygame.K_SPACE and not sorting:
                        sorting = True
                        if sorting_algorithm == merge_sort:
                            sorting_algorithm_generator = sorting_algorithm(draw_info, 0, len(lst) - 1, ascending)
                        else:
                            sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                        if not sound_enabled:
                            sound_enabled = play_sorting_sound(sorting_algo_name)
                    elif event.key == pygame.K_a and not sorting:
                        ascending = True
                    elif event.key == pygame.K_d and not sorting:
                        ascending = False
                    elif event.key == pygame.K_i and not sorting:
                        sorting_algorithm = insertion_sort
                        sorting_algo_name = "Insertion Sort"
                    elif event.key == pygame.K_b and not sorting:
                        sorting_algorithm = bubble_sort
                        sorting_algo_name = "Bubble Sort"
                    elif event.key == pygame.K_s and not sorting:
                        sorting_algorithm = selection_sort
                        sorting_algo_name = "Selection Sort"
                    elif event.key == pygame.K_m and not sorting:
                        sorting_algorithm = merge_sort
                        sorting_algo_name = "Merge Sort"
                    elif event.key == pygame.K_q and not sorting:
                        sorting_algorithm = quick_sort
                        sorting_algo_name = "Quick Sort"
                    elif event.key == pygame.K_x and not sorting:
                        sorting_algorithm = cocktail_shaker_sort
                        sorting_algo_name = "Cocktail Shaker Sort"
                    elif event.key == pygame.K_h and not sorting:
                        sorting_algorithm = heap_sort
                        sorting_algo_name = "Heap Sort"
                    elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS and not sorting:  # `+` or `=`
                        n = min(n + 10, 100)  # Cap the size at 100
                        lst = generate_starting_list(n, min_val, max_val)
                        draw_info.set_list(lst)
                    elif event.key == pygame.K_MINUS and not sorting:
                        n = max(n - 10, 10)  # Minimum size of 10
                        lst = generate_starting_list(n, min_val, max_val)
                        draw_info.set_list(lst)

            elif input_method == 'Mouse':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button in mouse_buttons:
                        if button['rect'].collidepoint(mouse_pos):
                            action = button['action']
                            print(f"Button '{button['text']}' pressed.")
                            if action == 'ascending':
                                ascending = True
                            elif action == 'descending':
                                ascending = False
                            elif action == 'new_list':
                                lst = generate_starting_list(n, min_val, max_val)
                                draw_info.set_list(lst)
                                sorting = False
                                if sound_enabled:
                                    pygame.mixer.music.stop()
                                    sound_enabled = False
                            elif action == 'increase_size':
                                n = min(n + 10, 100)  # Cap the size at 100
                                lst = generate_starting_list(n, min_val, max_val)
                                draw_info.set_list(lst)
                                sorting = False
                            elif action == 'decrease_size':
                                n = max(n - 10, 10)  # Minimum size of 10
                                lst = generate_starting_list(n, min_val, max_val)
                                draw_info.set_list(lst)
                                sorting = False
                            else:
                                sorting_algorithm = globals()[action]
                                sorting_algo_name = button['text']

                                if action == 'merge_sort':
                                    sorting_algorithm_generator = sorting_algorithm(draw_info, 0, len(lst) - 1,
                                                                                    ascending)
                                else:
                                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)

                                sorting = True
                                if not sound_enabled:
                                    print(f"Attempting to play sound for {sorting_algo_name}")
                                    sound_enabled = play_sorting_sound(sorting_algo_name)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
