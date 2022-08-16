import random
def get_sample():
    return random.random()*2-1

import multiprocessing

def check_inside_circle_batch(samples):
    return sum([(x**2 + y**2) <= 1 for x, y in samples])


def check_inside_circle(sample):
    x, y = sample
    return (x**2 + y**2) <= 1


def batch_samples(total, batch_size=int(1e5)):
    if total < batch_size:
        yield [(get_sample(), get_sample()) for j in range(int(total))]
    else:
        full_batches = total//batch_size
        for i in range(full_batches):
            yield [(get_sample(), get_sample()) for j in range(batch_size)]
        yield [(get_sample(), get_sample()) for j in range(total%batch_size)]


def calc_monte_carlo_pi(n_samples = 1e6):
    if n_samples > 1e7:
        with multiprocessing.Pool() as p:            
            circle_ratio = sum(p.map(check_inside_circle_batch, batch_samples(n_samples)))/n_samples        
    else:
        n_samples = int(n_samples)
        samples = [(get_sample(), get_sample()) for j in range(int(n_samples))]
        circle_ratio = sum([check_inside_circle(sample) for sample in samples])/n_samples
    square_area = 4
    pi = square_area * circle_ratio
    return pi