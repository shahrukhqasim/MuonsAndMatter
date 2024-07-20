


def convert_seconds(seconds):
    if seconds < 60:
        return f"{seconds} seconds"
    elif seconds < 3600:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{minutes} minutes and {remaining_seconds} seconds"
    else:
        hours = seconds // 3600
        remaining_seconds = seconds % 3600
        minutes = remaining_seconds // 60
        remaining_seconds = remaining_seconds % 60
        return f"{hours} hours, {minutes} minutes and {remaining_seconds} seconds"
