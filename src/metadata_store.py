import json


def save_metadata(
    metadata,
    path
):
    """
    Save chunk metadata to JSON file.
    """

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            metadata,
            f,
            ensure_ascii=False,
            indent=4
        )


def load_metadata(path):
    """
    Load chunk metadata from JSON file.
    """

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        metadata = json.load(f)

    return metadata