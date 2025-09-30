#!/bin/bash

# Usage: ./scan-with-yara.sh <folder_or_file_to_scan> <yara_rule_directory>

TARGET="$1"
YARA_RULE_DIR="$2"

RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
NC='\033[0m' # No Color

if [[ -z "$TARGET" || -z "$YARA_RULE_DIR" ]]; then
    echo "Usage: $0 <folder_or_file_to_scan> <yara_rule_directory>"
    exit 1
fi

if [[ ! -e "$TARGET" ]]; then
    echo "Target to scan does not exist: $TARGET"
    exit 2
fi

if [[ ! -d "$YARA_RULE_DIR" ]]; then
    echo "Yara rule directory does not exist: $YARA_RULE_DIR"
    exit 3
fi

find "$YARA_RULE_DIR" -type f -name "*.yar" | while read -r RULE_FILE; do
    echo "Using rule $(basename "$RULE_FILE")..."

    if [[ -d "$TARGET" ]]; then
        FILES_TO_SCAN=$(find "$TARGET" -type f)
    elif [[ -f "$TARGET" ]]; then
        FILES_TO_SCAN="$TARGET"
    else
        echo -e "${ORANGE}Target is neither a file nor a directory: $TARGET${NC}"
        continue
    fi

    # Scan each file
    while read -r TARGET_FILE; do
        # If no files found, skip
        [[ -z "$TARGET_FILE" ]] && continue
        echo "Scanning $TARGET_FILE with rule $(basename "$RULE_FILE")..."
        OUTPUT=$(yara "$RULE_FILE" "$TARGET_FILE" 2>&1)
        STATUS=$?
        if [[ $STATUS -eq 0 ]]; then
            echo -e "${RED}Rule: $(basename "$RULE_FILE") - Match found in $TARGET_FILE:${NC}"
            echo -e "${RED}${OUTPUT}${NC}"
        elif [[ $STATUS -eq 1 ]]; then
            echo -e "${GREEN}Rule: $(basename "$RULE_FILE") - No match in $TARGET_FILE.${NC}"
        else
            echo -e "${ORANGE}Rule: $(basename "$RULE_FILE") - Error (skipped for $TARGET_FILE): $OUTPUT${NC}"
        fi
    done <<< "$FILES_TO_SCAN"
done