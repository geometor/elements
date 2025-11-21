#!/bin/bash

# Check if a book ID was provided
if [ -z "$1" ]; then
  echo "Usage: $0 <book_id>"
  echo "Example: $0 I"
  exit 1
fi

BOOK_ID=$1

# Run the scan script
echo "----------------------------------------"
echo "Scanning propositions for Book $BOOK_ID..."
echo "----------------------------------------"
python src/geometor/elements/ingest/scan_propositions.py --book "$BOOK_ID"

# Check if scan was successful (optional, but good practice)
if [ $? -ne 0 ]; then
  echo "Scanning failed."
  exit 1
fi

# Run the stitch script
echo "----------------------------------------"
echo "Stitching propositions for Book $BOOK_ID..."
echo "----------------------------------------"
python src/geometor/elements/ingest/stitch_propositions.py --book "$BOOK_ID"

echo "----------------------------------------"
echo "Process complete for Book $BOOK_ID."
