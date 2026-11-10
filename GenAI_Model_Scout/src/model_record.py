# GenAI Model Scout
# Feature 1: Manage and analyze multiple model records


# Sample model data
# These are dummy records, not live Hugging Face data.

models = [
    {
        "model_id": "example-org/compact-text-model",
        "task": "text-generation",
        "downloads": 125_000,
        "likes": 850,
        "is_private": False
    },
    {
        "model_id": "example-org/vision-helper",
        "task": "image-to-text",
        "downloads": 50_000,
        "likes": 320,
        "is_private": False
    },
    {
        "model_id": "example-org/large-language-model",
        "task": "text-generation",
        "downloads": 1_500_000,
        "likes": 9_800,
        "is_private": False
    },
    {
        "model_id": "example-org/internal-model",
        "task": "text-generation",
        "downloads": 750_000,
        "likes": 4_100,
        "is_private": True
    }
]
# Fixed order of fields for displaying model information
SUMMARY_FIELDS = (
    "model_id",
    "task",
    "downloads",
    "likes",
    "visibility",
    "popularity"
)


def classify_popularity(downloads):
    if downloads >= 1_000_000:
        return "very popular"
    elif downloads >= 100_000:
        return "growing"
    else:
        return "early-stage"


def build_model_summary(model):

    if model["is_private"]:
        visibility = "private"
    else:
        visibility = "public"

    return {
        "model_id": model["model_id"],
        "task": model["task"],
        "downloads": model["downloads"],
        "likes": model["likes"],
        "visibility": visibility,
        "popularity": classify_popularity(model["downloads"])
    }

def filter_models(
        models,
        task=None,
        min_downloads=0,
        include_private=False
):
    filtered_models = []

    for model in models:
        #Filter by task
        if task is not None and model["task"] != task:
            continue

        # Filter by minimum downloads
        if model["downloads"] < min_downloads:
            continue

        # Exclude private models by default
        if not include_private and model["is_private"]:
            continue

        filtered_models.append(model)

    return filtered_models

def get_available_tasks(models):
    available_tasks = {
        model["task"]
        for model in models
    }
    return sorted(available_tasks)

def count_models_by_task(models):
    task_counts = {}
    for model in models:
        task = model["task"]

        task_counts[task] = task_counts.get(task, 0) + 1

    return task_counts

# Generate summaries for all models
model_summaries = [
    build_model_summary(model)
    for model in models
]

# Display all model summaries
print("\n========== GENAI MODEL SCOUT ==========")

for model in model_summaries:
    print()

    for field in SUMMARY_FIELDS:
        print(f"{field.replace('_', ' ').title()}: {model[field]}")


# Display shortlisted models
# Search 1: Find all text-generation models
text_models = filter_models(
    models,
    task="text-generation"
)

# Search 2: Find public models with at least 100,000 downloads
popular_models = filter_models(
    models,
    min_downloads=100_000
)

# Search 3: Find all models, including private models
all_models = filter_models(
    models,
    include_private=True
)

print("\n========== TEXT GENERATION MODELS ==========")

for model in text_models:
    print(model["model_id"])


print("\n========== POPULAR PUBLIC MODELS ==========")

for model in popular_models:
    print(model["model_id"])


print("\n========== ALL MODELS ==========")

for model in all_models:
    print(model["model_id"])


# Generate inventory reports
available_tasks = get_available_tasks(models)
task_counts = count_models_by_task(models)

# Display unique tasks
print(f"\n {"=" * 10} AVAILABLE TASKS {"=" * 10}")
for task in available_tasks:
    print(task)

# Display model count by task
print(f"\n{"=" * 10} MODELS BY TASK {"=" * 10}")

for task, count in task_counts.items():
    print(f"{task}: {count} models")