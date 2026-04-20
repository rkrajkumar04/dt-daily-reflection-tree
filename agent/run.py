#!/usr/bin/env python3

import json
import sys
from pathlib import Path


AXES = {
    "axis1": ("external", "internal"),
    "axis2": ("entitlement", "contribution"),
    "axis3": ("self", "altrocentric"),
}


def load_tree(tree_path: Path) -> dict:
    with tree_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_index(tree: dict) -> dict:
    return {node["id"]: node for node in tree["nodes"]}


def init_state(tree: dict) -> dict:
    state = {"answers": {}, "signals": {}}
    for axis, poles in AXES.items():
        state["signals"][axis] = {poles[0]: 0, poles[1]: 0}
    state["axis_labels"] = tree["meta"]["axes"]
    return state


def apply_signals(option: dict, state: dict) -> None:
    for signal in option.get("signals", []):
        axis, pole = signal.split(":", 1)
        state["signals"][axis][pole] += 1


def dominant(axis: str, state: dict) -> str:
    left, right = AXES[axis]
    left_score = state["signals"][axis][left]
    right_score = state["signals"][axis][right]
    return right if right_score >= left_score else left


def interpolate(text: str, state: dict) -> str:
    rendered = text

    for node_id, answer in state["answers"].items():
        rendered = rendered.replace("{" + node_id + ".answer}", answer)

    for axis in AXES:
        dom = dominant(axis, state)
        label = state["axis_labels"][axis]["labels"][dom]
        rendered = rendered.replace("{" + axis + ".dominant}", dom)
        rendered = rendered.replace("{" + axis + ".dominantLabel}", label)

    return rendered


def choose_option(node: dict) -> dict:
    print()
    print(node["text"])
    for idx, option in enumerate(node["options"], start=1):
        print(f"{idx}. {option['label']}")

    while True:
        raw = input("> ").strip()
        if raw.isdigit():
            idx = int(raw)
            if 1 <= idx <= len(node["options"]):
                return node["options"][idx - 1]
        print("Please enter a valid option number.")


def decide(node: dict, state: dict) -> str:
    for rule in node["rules"]:
        source = rule.get("source")
        if source and "ifAnswerIn" in rule:
            if state["answers"].get(source) in rule["ifAnswerIn"]:
                return rule["target"]
        if "ifDominant" in rule:
            axis = rule["ifDominant"]["axis"]
            value = rule["ifDominant"]["value"]
            if dominant(axis, state) == value:
                return rule["target"]
    raise ValueError(f"No matching decision rule for node {node['id']}")


def run(tree: dict) -> None:
    nodes = build_index(tree)
    state = init_state(tree)
    current_id = tree["startId"]

    while current_id:
        node = nodes[current_id]
        node_type = node["type"]

        if node_type in {"start", "bridge"}:
            print()
            print(interpolate(node["text"], state))
            current_id = node.get("next")
            continue

        if node_type == "question":
            question_text = interpolate(node["text"], state)
            node_to_show = dict(node)
            node_to_show["text"] = question_text
            selected = choose_option(node_to_show)
            state["answers"][node["id"]] = selected["label"]
            apply_signals(selected, state)
            current_id = node.get("next")
            continue

        if node_type == "decision":
            current_id = decide(node, state)
            continue

        if node_type in {"reflection", "summary", "end"}:
            print()
            print(interpolate(node["text"], state))
            if node_type == "end":
                break
            if node_type == "reflection":
                input("\nPress Enter to continue...")
            current_id = node.get("next")
            continue

        raise ValueError(f"Unsupported node type: {node_type}")


def main() -> int:
    default_tree = Path(__file__).resolve().parents[1] / "tree" / "reflection-tree.json"
    tree_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_tree

    if not tree_path.exists():
        print(f"Tree file not found: {tree_path}", file=sys.stderr)
        return 1

    tree = load_tree(tree_path)
    run(tree)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
