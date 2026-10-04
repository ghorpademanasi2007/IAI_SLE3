# Contribution Log – IAI_SLE3

## Project

**SLE-3: Architectural Design using Full C4 Model**  
**Course:** 02AML204 – Introduction to Artificial Intelligence  
**System:** Graph Search System using BFS and DFS

---

## Contribution Summary

| Contributor | Contribution |
|---|---|
| **Student – Manasi Ghorpade** | Selected the graph-search system continued from SLE-2; reviewed the BFS/DFS structure; decided the main containers; reviewed the component responsibilities; checked the final architecture and documentation. |
| **AI – ChatGPT** | Helped organize the architecture according to the C4 Model; suggested concise container/component descriptions; prepared Mermaid diagram structure; helped format the README and contribution log. |

## Work Breakdown

### 1. System Selection
- Continued the graph-search system from SLE-2.
- Used BFS and DFS as the two search strategies.
- Kept the architecture small and suitable for an academic SLE submission.

### 2. Context Level
- Identified the User / Operator as the external actor.
- Defined the Graph Search System as the main system boundary.
- Identified user input and search results as the main interactions.

### 3. Container Level
- Identified four main containers:
  - Input Module
  - Search Engine
  - Graph & Visited Memory
  - Output Module
- Reviewed the responsibility of each container.

### 4. Component Level
- Selected the Search Engine as the main container for decomposition.
- Identified Algorithm Controller, Frontier / Recursion Control, Visited Set Manager, Goal Test and Path Reconstructor.

### 5. Code Level
- Mapped the architecture to the important BFS and DFS functions.
- Kept the Code level limited to names and responsibilities instead of large source-code blocks.

### 6. Documentation
- Created `C4_ARCHITECTURE.md`.
- Updated `README.md`.
- Created this contribution log.
- Added Mermaid diagrams for the four-level architecture and overall flow.

---

## AI Contribution / Ownership Note

AI was used as a supporting tool, not as a replacement for understanding the project. The student reviewed the proposed architecture and is responsible for the final repository content and for explaining the design during evaluation.

The SLE-3 guideline specifically requires an honest AI contribution note and checks whether the student understands the design choices. Therefore, AI assistance is recorded here clearly.

---

## Final Status

- [x] System selected from previous search work
- [x] Context architecture completed
- [x] Container architecture completed
- [x] Component architecture completed
- [x] Code-level overview completed
- [x] Design decisions documented
- [x] AI contribution documented
- [x] README added/updated
- [x] Contribution log added
