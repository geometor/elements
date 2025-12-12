# GEOMETOR Elements

A digital reconstruction of Euclid's Elements for dependency mapping and analysis.

## Overview

`geometor.elements` builds upon the semantic structure provided by `geometor.euclid` to create the **G Index**—a symbolic and logical codification of the geometric constructions.

It is responsible for:
-   **G Index Generation**: Creating a dependency-aware index of all propositions.
-   **Codification**: Translating text descriptions into symbolic GEOMETOR models.
-   **Visualization**: Rendering the "Genealogy" of geometric truth.

## Key Repos

-   **elements**: This repository. Code for G Index generation and model codification.
-   **euclid**: The source of truth for the text and logical graph.

## Development Plan

-   Refine `g_index` generation logic.
-   Implement initial codification of Book I propositions.

## Workflows

### Create Branch

1.  **Navigate to Repository**: `cd /home/phi/PROJECTS/geometor/elements`
2.  **Checkout Main**: `git checkout main`
3.  **Pull Latest**: `git pull origin main`
4.  **Create Branch**: `git checkout -b <branch_name>`