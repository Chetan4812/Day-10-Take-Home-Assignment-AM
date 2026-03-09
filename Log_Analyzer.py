from collections import Counter, defaultdict

logs = [
"2026-03-09 10:15:23,INFO,auth,User login successful",
"2026-03-09 10:16:01,ERROR,payment,Payment gateway timeout",
"2026-03-09 10:16:45,WARNING,auth,Multiple login attempts",
"2026-03-09 10:17:10,INFO,inventory,Stock updated",
"2026-03-09 10:17:55,ERROR,payment,Payment gateway timeout",
"2026-03-09 10:18:20,CRITICAL,server,Database connection lost",
"2026-03-09 10:19:02,INFO,auth,User logout",
"2026-03-09 10:19:50,ERROR,inventory,Stock update failed",
"2026-03-09 10:20:33,WARNING,server,High memory usage",
"2026-03-09 10:21:10,INFO,payment,Payment processed",
]

def parse_log(line):
    """Convert log line into dictionary"""
    
    try:
        timestamp, level, module, message = line.split(",", 3)
        
        return {
            "timestamp": timestamp,
            "level": level,
            "module": module,
            "message": message
        }
    
    except ValueError:
        return None


def analyze_logs(log_lines):

    parsed_logs = []
    
    level_counter = Counter()
    module_counter = Counter()
    error_messages = Counter()
    
    errors_by_module = defaultdict(list)

    for line in log_lines:

        log = parse_log(line)
        if not log:
            continue

        parsed_logs.append(log)

        level = log.get("level")
        module = log.get("module")
        message = log.get("message")

        level_counter[level] += 1
        module_counter[module] += 1

        if level in ["ERROR", "CRITICAL"]:
            error_messages[message] += 1
            errors_by_module[module].append(message)

    total_entries = len(parsed_logs)
    total_errors = level_counter["ERROR"] + level_counter["CRITICAL"]

    error_rate = (total_errors / total_entries * 100) if total_entries else 0

    summary = {
        "total_entries": total_entries,
        "error_rate": round(error_rate, 2),
        "top_errors": error_messages.most_common(3),
        "busiest_module": module_counter.most_common(1)[0][0] if module_counter else None
    }

    return {
        "parsed_logs": parsed_logs,
        "log_level_distribution": dict(level_counter),
        "most_active_modules": module_counter.most_common(),
        "most_common_errors": error_messages.most_common(),
        "errors_by_module": dict(errors_by_module),
        "summary": summary
    }


result = analyze_logs(logs)

print(result["summary"])