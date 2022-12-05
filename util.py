import os

def open_input(day, sample_mode):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    ext = '.sample' if sample_mode else '.input'
    return open(os.path.join(dir_path, 'inputs', f"{day}{ext}"))


def read_input_lines(day, sample_mode):
    return [_.strip() for _ in open_input(day, sample_mode).readlines()]

def read_input_raw(day, sample_mode):
    return open_input(day, sample_mode).read()