# === Stage 28: Add overdue item detection based on due dates ===
# Project: GardenPlot
def detect_overdue_items(garden):
    """Return list of task items whose due date has passed.
    
    Args:
        garden: dict with 'tasks' list and 'current_date' string.
        
    Returns:
        list of overdue task dicts.
    """
    overdue = []
    today = garden['current_date']
    for task in garden['tasks']:
        if task.get('due_date') and task['due_date'] < today:
            task['status'] = 'overdue'
            overdue.append(task)
    return overdue
