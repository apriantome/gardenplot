# === Stage 61: Add performance timing for core list and search operations ===
# Project: GardenPlot
import time

def time_operation(func, *args, repeats=1):
    results = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - start
        results.append((elapsed, result))
    return results

def benchmark_search(bed_plantings, query, repeats=1):
    benchmarks = []
    for _ in range(repeats):
        start = time.perf_counter()
        matches = [p for p in bed_plantings if query.lower() in p['plant'].lower() or query.lower() in p['note'].lower()]
        elapsed = time.perf_counter() - start
        benchmarks.append((elapsed, len(matches), matches))
    return benchmarks

def benchmark_list_operations(bed_plantings, repeats=1):
    benchmarks = []
    for _ in range(repeats):
        start = time.perf_counter()
        total = len(bed_plantings)
        unique_plants = len(set(p['plant'] for p in bed_plantings))
        with_water = len([p for p in bed_plantings if p.get('watered')])
        elapsed = time.perf_counter() - start
        benchmarks.append((elapsed, total, unique_plants, with_water))
    return benchmarks

def time_all_operations(bed_plantings, query):
    timing = {}
    timing['search'] = time_operation(lambda: benchmark_search(bed_plantings, query), repeats=1)
    timing['list'] = time_operation(lambda: benchmark_list_operations(bed_plantings), repeats=1)
    return timing

def print_benchmarks(operation, benchmarks):
    for i, (elapsed, *values) in enumerate(benchmarks):
        if operation == 'search':
            print(f"Run {i+1}: {elapsed*1000:.3f}ms, matches={values[0]}")
        elif operation == 'list':
            print(f"Run {i+1}: {elapsed*1000:.3f}ms, total={values[0]}, unique={values[1]}, watered={values[2]}")

def report_performance(bed_plantings, query):
    print(f"Performance report for {len(bed_plantings)} plantings")
    print(f"Searching for '{query}'")
    benchmarks = benchmark_search(bed_plantings, query)
    print_benchmarks('search', benchmarks)
    benchmarks = benchmark_list_operations(bed_plantings)
    print_benchmarks('list', benchmarks)
    return benchmarks
