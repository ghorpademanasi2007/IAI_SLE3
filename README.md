# IAI_SLE3 – Architectural Design using Full C4 Model

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**SLE:** 3 – Architectural Design using Full C4 Model  
**System:** Graph Search System using BFS and DFS  

## 1. Project Overview

This repository contains the SLE-3 architectural design for the graph search system continued from SLE-2. The system demonstrates Breadth-First Search (BFS) and Depth-First Search (DFS) on a simple graph and represents its architecture using all four levels of the C4 Model.

The SLE-3 guideline asks students to continue from the SLE-2 search/maze/agent work and show the architecture at Context, Container, Component, and Code levels. fileciteturn0file0L29-L35

## 2. C4 Model Used

| Level | Architecture View | This Project |
|---|---|---|
| Level 1 | Context | User interacts with the Graph Search System |
| Level 2 | Container | Input Module, Search Engine, Graph/Visited Memory, Output Module |
| Level 3 | Component | BFS/DFS control, Frontier, Visited Set, Goal Test, Path Reconstruction |
| Level 4 | Code | `bfs_search()`, `dfs_search()`, graph data, timing functions and output functions |

The guideline defines C4 as **Context, Container, Component, Code** and requires all four levels. fileciteturn0file0L16-L28

## 3. Repository Files

- `C4_ARCHITECTURE.md` – complete Level 1 to Level 4 architecture with Mermaid diagrams and explanations.
- `CONTRIBUTION_LOG.md` – contribution and AI-use log for the SLE-3 work.
- `README.md` – project overview, structure and usage notes.

## 4. System Description

The Graph Search System accepts a graph, starting node and target node from the user. The Search Engine applies BFS or DFS to explore the graph. A visited set prevents repeated exploration, while the search process produces a path and the number of explored nodes. The result is then displayed to the user.

The graph and BFS/DFS implementation are continued conceptually from the SLE-2 search work. In SLE-2, BFS uses a queue and visited set, while DFS uses recursive traversal and a visited set.

## 5. Design Decisions

1. BFS and DFS are grouped under one Search Engine because both solve the same graph-search problem with different traversal strategies.
2. The architecture is intentionally kept small and readable, following the SLE-3 requirement of about 4–7 containers.
3. The Component diagram focuses on the Search Engine, which is the main processing container.
4. The Code level lists important functions rather than pasting large source-code blocks.

## 6. AI Contribution

AI was used as a support tool for organizing the C4 architecture, improving documentation structure, preparing Mermaid diagrams, and checking that the submission covers the required four C4 levels. The student remains responsible for reviewing, understanding and explaining the final architecture.

## 7. Reference

The architecture follows the provided SLE-3 Student Guideline for **02AML204 – Introduction to Artificial Intelligence**, including the required Context, Container, Component and Code levels, design decisions, AI contribution note and conclusion. fileciteturn0file0L87-L129
