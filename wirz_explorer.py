"""
Wirz Concept Explorer
A semantic database explorer for cross-disciplinary concept understanding.
Built as the first Python component of the Wirz Engine.

AP CSP Post-Exam Project - Track 1: The App Builders
Requirements met:
- User Interface: Clean CLI with intuitive navigation
- Code Complexity: Sequencing, selection, iteration + parameterized functions
- Documentation: README.md included
"""

# =============================================================================
# WIRZ CONCEPT DATABASE - Sample data for demonstration
# =============================================================================

CONCEPTS = {
    "loneliness": {
        "definition": "A complex emotional response to isolation or lack of connection",
        "domain": ["psychology", "emotion", "social"],
        "related": ["solitude", "isolation", "belonging", "attachment"],
        "causes": ["social_rejection", "loss", "displacement"],
        "effects": ["depression", "creativity", "self_reflection"]
    },
    "solitude": {
        "definition": "The state of being alone, often chosen and potentially enriching",
        "domain": ["psychology", "philosophy", "emotion"],
        "related": ["loneliness", "meditation", "introspection", "silence"],
        "causes": ["voluntary_withdrawal", "environment"],
        "effects": ["self_discovery", "creativity", "peace"]
    },
    "causality": {
        "definition": "The relationship between cause and effect; how one event influences another",
        "domain": ["logic", "philosophy", "science"],
        "related": ["correlation", "determinism", "inference", "chain"],
        "causes": ["observation", "reasoning"],
        "effects": ["prediction", "understanding", "control"]
    },
    "semantics": {
        "definition": "The study of meaning in language, symbols, and expression",
        "domain": ["linguistics", "logic", "cognition"],
        "related": ["syntax", "pragmatics", "meaning", "reference"],
        "causes": ["language_development", "cognition"],
        "effects": ["communication", "translation", "comprehension"]
    },
    "cognition": {
        "definition": "The mental processes involved in gaining knowledge and comprehension",
        "domain": ["psychology", "neuroscience", "philosophy"],
        "related": ["perception", "memory", "reasoning", "attention"],
        "causes": ["brain_activity", "sensory_input", "experience"],
        "effects": ["decision_making", "learning", "problem_solving"]
    },
    "translation": {
        "definition": "The process of rendering text or meaning from one language to another",
        "domain": ["linguistics", "communication", "culture"],
        "related": ["semantics", "equivalence", "interpretation", "context"],
        "causes": ["multilingualism", "cultural_contact", "need"],
        "effects": ["cross_cultural_understanding", "loss", "creation"]
    },
    "creativity": {
        "definition": "The ability to generate novel and valuable ideas or solutions",
        "domain": ["psychology", "cognition", "art"],
        "related": ["imagination", "innovation", "expression", "divergence"],
        "causes": ["constraint", "solitude", "inspiration", "cognitive_flexibility"],
        "effects": ["art", "invention", "self_expression", "problem_solving"]
    },
    "metaphor": {
        "definition": "A figure of speech that describes something by referring to something else",
        "domain": ["linguistics", "cognition", "literature"],
        "related": ["analogy", "symbolism", "conceptual_blending", "language"],
        "causes": ["cognitive_mapping", "communication_need"],
        "effects": ["understanding", "conceptual_extension", "expression"]
    },
    "empathy": {
        "definition": "The ability to understand and share the feelings of another",
        "domain": ["psychology", "emotion", "social"],
        "related": ["compassion", "theory_of_mind", "connection", "emotion"],
        "causes": ["social_bonding", "mirror_neurons", "experience"],
        "effects": ["relationships", "morality", "communication", "healing"]
    },
    "abstraction": {
        "definition": "The process of extracting common properties from specific instances",
        "domain": ["logic", "cognition", "computer_science"],
        "related": ["generalization", "concept", "model", "pattern"],
        "causes": ["cognitive_development", "problem_solving_need"],
        "effects": ["theory", "efficiency", "understanding", "computation"]
    }
}


# =============================================================================
# USER INTERFACE FUNCTIONS
# =============================================================================

def print_header(title):
    """Display a formatted section header. Parameter: title (string)"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def print_menu():
    """Display the main navigation menu."""
    print_header("WIRZ CONCEPT EXPLORER")
    print("""
  Explore how concepts connect across disciplines
  through causal chains and semantic relationships.

  [1]  Search for a concept
  [2]  Browse all concepts
  [3]  Explore causal chain (A → B)
  [4]  Find path between concepts
  [5]  Add a new concept
  [6]  Compare two concepts
  [7]  About Wirz
  [0]  Exit
""")


def print_concept_card(name, concept):
    """
    Display a formatted concept card.
    Parameters: name (string), concept (dictionary)
    Uses: iteration (for loops) to display lists
    """
    print(f"\n  ┌{'─' * 50}┐")
    print(f"  │  {name.upper():48}│")
    print(f"  ├{'─' * 50}┤")
    print(f"  │  Definition: {concept['definition'][:38]:38}│")
    if len(concept['definition']) > 38:
        remaining = concept['definition'][38:]
        for i in range(0, len(remaining), 38):
            line = remaining[i:i + 38]
            print(f"  │              {line:38}│")

    domains = ", ".join(concept['domain'])
    print(f"  ├{'─' * 50}┤")
    print(f"  │  Domains:    {domains:38}│")

    # Iteration: loop through related concepts
    related = ", ".join(concept['related'])
    print(f"  │  Related:    {related[:38]:38}│")
    if len(related) > 38:
        extra = related[38:]
        for i in range(0, len(extra), 38):
            print(f"  │              {extra[i:i + 38]:38}│")

    print(f"  ├{'─' * 50}┤")
    print(f"  │  CAUSES:")
    for cause in concept['causes']:  # Iteration
        print(f"  │      → {cause:42}│")
    print(f"  │  EFFECTS:")
    for effect in concept['effects']:  # Iteration
        print(f"  │      ⇒ {effect:42}│")

    print(f"  └{'─' * 50}┘")


# =============================================================================
# CORE ALGORITHM FUNCTIONS
# =============================================================================

def search_concept(query):
    """
    Search for a concept by name or partial match.
    Parameter: query (string) - search term
    Returns: list of matching concept names
    Uses: iteration (for loop), selection (if with in operator)
    """
    matches = []
    query_lower = query.lower().strip()

    # Iteration: loop through all concepts
    for name in CONCEPTS:
        # Selection: check if query matches name or definition
        if query_lower in name.lower() or query_lower in CONCEPTS[name]["definition"].lower():
            matches.append(name)
        else:
            # Also check domains
            for domain in CONCEPTS[name]["domain"]:
                if query_lower in domain.lower() and name not in matches:
                    matches.append(name)

    return matches


def find_causal_chain(start_concept, steps=3):
    """
    Trace a causal chain forward from a starting concept.
    Parameters: start_concept (string), steps (integer, default 3)
    Returns: list representing the causal chain
    Uses: sequencing, selection (if), iteration (for/while)
    """
    chain = []
    current = start_concept

    # Sequencing: build chain step by step
    for step in range(steps):
        # Selection: check if current concept exists
        if current not in CONCEPTS:
            break

        concept = CONCEPTS[current]
        chain.append(current)

        # Selection: pick the next concept from effects
        if concept["effects"]:
            # Pick first effect that exists in database
            next_found = False
            for effect in concept["effects"]:
                if effect in CONCEPTS and effect not in chain:
                    current = effect
                    next_found = True
                    break
            if not next_found:
                break
        else:
            break

    return chain


def find_path_between(start, end, max_depth=5):
    """
    Find a path between two concepts using breadth-first search.
    Parameters: start (string), end (string), max_depth (integer)
    Returns: list representing the path, or empty list if no path found
    Uses: sequencing (BFS algorithm), selection, iteration
    """
    if start not in CONCEPTS or end not in CONCEPTS:
        return []

    if start == end:
        return [start]

    # BFS - uses iteration and sequencing
    queue = [(start, [start])]
    visited = {start}

    while queue and len(queue[0][1]) <= max_depth:
        current, path = queue.pop(0)

        # Get neighbors: effects, causes, and related
        neighbors = []
        if current in CONCEPTS:
            neighbors.extend(CONCEPTS[current]["effects"])
            neighbors.extend(CONCEPTS[current]["causes"])
            neighbors.extend(CONCEPTS[current]["related"])

        # Iteration: check each neighbor
        for neighbor in neighbors:
            if neighbor == end:
                return path + [neighbor]

            # Selection: only visit each node once
            if neighbor not in visited and neighbor in CONCEPTS:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []


def compare_concepts(name1, name2):
    """
    Compare two concepts and show their relationships.
    Parameters: name1 (string), name2 (string)
    Uses: iteration, selection
    """
    if name1 not in CONCEPTS or name2 not in CONCEPTS:
        print("  One or both concepts not found.")
        return

    c1 = CONCEPTS[name1]
    c2 = CONCEPTS[name2]

    # Find shared domains
    shared_domains = []
    for d in c1["domain"]:
        if d in c2["domain"]:
            shared_domains.append(d)

    # Find direct connections
    direct = name2 in c1["related"] or name1 in c2["related"]
    c1_to_c2 = name2 in c1["effects"]
    c2_to_c1 = name1 in c2["effects"]

    print(f"\n  {'─' * 50}")
    print(f"  COMPARING: {name1.upper()}  vs  {name2.upper()}")
    print(f"  {'─' * 50}")

    # Selection: check domain overlap
    if shared_domains:
        print(f"  Shared domains: {', '.join(shared_domains)}")
    else:
        print(f"  No shared domains")
        print(f"  {name1}: {', '.join(c1['domain'])}")
        print(f"  {name2}: {', '.join(c2['domain'])}")

    # Selection: check direct connections
    print(f"\n  Direct connections:")
    if direct:
        print(f"    ✓ Related concepts")
    if c1_to_c2:
        print(f"    → {name1} CAUSES {name2}")
    if c2_to_c1:
        print(f"    → {name2} CAUSES {name1}")
    if not any([direct, c1_to_c2, c2_to_c1]):
        print(f"    No direct connection in database")

    # Find path between them
    path = find_path_between(name1, name2)
    if path and len(path) > 1:
        print(f"\n  Connection path:")
        print(f"    {' → '.join(path)}")


# =============================================================================
# USER INTERACTION FUNCTIONS
# =============================================================================

def handle_search():
    """Handle the concept search feature."""
    print_header("SEARCH CONCEPTS")
    query = input("  Enter search term: ").strip()

    # Selection: check for empty input
    if not query:
        print("  Please enter a search term.")
        return

    matches = search_concept(query)

    # Selection: handle results
    if len(matches) == 0:
        print(f"  No concepts found matching '{query}'.")
    elif len(matches) == 1:
        print_concept_card(matches[0], CONCEPTS[matches[0]])
    else:
        print(f"  Found {len(matches)} matches:")
        for i, name in enumerate(matches, 1):
            print(f"    {i}. {name}")
        choice = input("  Select number (or press Enter for all): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(matches):
            name = matches[int(choice) - 1]
            print_concept_card(name, CONCEPTS[name])
        else:
            for name in matches:
                print_concept_card(name, CONCEPTS[name])


def handle_browse():
    """Handle browsing all concepts."""
    print_header("ALL CONCEPTS")
    concepts_list = sorted(CONCEPTS.keys())

    # Iteration: display numbered list
    for i, name in enumerate(concepts_list, 1):
        domains = ", ".join(CONCEPTS[name]["domain"])
        print(f"  {i:2}. {name:20} [{domains}]")

    choice = input("\n  Enter number to view details (or press Enter to go back): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(concepts_list):
        name = concepts_list[int(choice) - 1]
        print_concept_card(name, CONCEPTS[name])


def handle_causal_chain():
    """Handle the causal chain exploration feature."""
    print_header("EXPLORE CAUSAL CHAIN")
    print(f"  Available concepts: {', '.join(sorted(CONCEPTS.keys()))}")
    name = input("  Enter starting concept: ").strip().lower()

    # Selection: validate input
    if name not in CONCEPTS:
        print(f"  Concept '{name}' not found.")
        return

    steps_input = input("  Number of steps (default 3): ").strip()
    steps = int(steps_input) if steps_input.isdigit() else 3

    chain = find_causal_chain(name, steps)

    # Selection: display results
    if len(chain) > 1:
        print(f"\n  Causal chain from '{name}':")
        for i in range(len(chain) - 1):
            c1 = CONCEPTS[chain[i]]
            print(f"    [{i+1}] {chain[i]}")
            # Find the specific effect
            for effect in c1["effects"]:
                if effect == chain[i + 1]:
                    print(f"         └── causes → {effect}")
                    break
        print(f"    [{len(chain)}] {chain[-1]}")
    else:
        print(f"  No extended chain found from '{name}'.")
        print_concept_card(name, CONCEPTS[name])


def handle_find_path():
    """Handle finding a path between two concepts."""
    print_header("FIND PATH BETWEEN CONCEPTS")
    print(f"  Available: {', '.join(sorted(CONCEPTS.keys()))}")
    start = input("  Start concept: ").strip().lower()
    end = input("  End concept: ").strip().lower()

    # Selection: validate inputs
    if start not in CONCEPTS:
        print(f"  '{start}' not found.")
        return
    if end not in CONCEPTS:
        print(f"  '{end}' not found.")
        return

    path = find_path_between(start, end)

    # Selection: display result
    if path:
        print(f"\n  Path found ({len(path)} steps):")
        print(f"    {' → '.join(path)}")
    else:
        print(f"\n  No path found between '{start}' and '{end}' within depth limit.")


def handle_add_concept():
    """Handle adding a new concept to the database."""
    print_header("ADD NEW CONCEPT")
    name = input("  Concept name (no spaces, use_underscores): ").strip().lower()

    # Selection: validate name
    if not name:
        print("  Name cannot be empty.")
        return
    if name in CONCEPTS:
        print(f"  '{name}' already exists.")
        return

    definition = input("  Definition: ").strip()
    if not definition:
        print("  Definition cannot be empty.")
        return

    domains_input = input("  Domains (comma-separated): ").strip()
    domain = [d.strip() for d in domains_input.split(",") if d.strip()]

    related_input = input("  Related concepts (comma-separated): ").strip()
    related = [r.strip() for r in related_input.split(",") if r.strip()]

    causes_input = input("  Causes (comma-separated): ").strip()
    causes = [c.strip() for c in causes_input.split(",") if c.strip()]

    effects_input = input("  Effects (comma-separated): ").strip()
    effects = [e.strip() for e in effects_input.split(",") if e.strip()]

    # Sequencing: construct and add the new concept
    CONCEPTS[name] = {
        "definition": definition,
        "domain": domain if domain else ["general"],
        "related": related,
        "causes": causes,
        "effects": effects
    }

    print(f"\n  ✓ Concept '{name}' added successfully!")
    print_concept_card(name, CONCEPTS[name])


def handle_compare():
    """Handle the concept comparison feature."""
    print_header("COMPARE TWO CONCEPTS")
    print(f"  Available: {', '.join(sorted(CONCEPTS.keys()))}")
    name1 = input("  First concept: ").strip().lower()
    name2 = input("  Second concept: ").strip().lower()
    compare_concepts(name1, name2)


def show_about():
    """Display information about Wirz."""
    print_header("ABOUT WIRZ")
    print("""
  Wirz Engine is a semantic database for cross-disciplinary
  understanding of concepts via causal chains.

  This Concept Explorer is the first Python component,
  built to demonstrate:
    - Concept storage and retrieval
    - Causal chain traversal
    - Semantic relationship mapping
    - Cross-domain concept linking

  Future modules: Interex (writer's perspective tool),
  cognAIz (cognitive typology AI collaboration).

  Built for: AP Computer Science Principles
  Author: [Your Name]
  Date: June 2026
""")


# =============================================================================
# MAIN PROGRAM - SEQUENCING: THE OVERALL FLOW
# =============================================================================

def main():
    """
    Main program loop.
    Sequencing: initialize → display menu → process choice → repeat
    """
    print("\n" + "=" * 60)
    print("  Welcome to the Wirz Concept Explorer!")
    print("=" * 60)
    print(f"  Loaded {len(CONCEPTS)} concepts across multiple domains.")
    print("  Type '0' at any time to return to the menu.")

    running = True

    # Iteration: main program loop
    while running:
        print_menu()
        choice = input("  Enter your choice [0-7]: ").strip()

        # Selection: route to appropriate handler
        if choice == "1":
            handle_search()
        elif choice == "2":
            handle_browse()
        elif choice == "3":
            handle_causal_chain()
        elif choice == "4":
            handle_find_path()
        elif choice == "5":
            handle_add_concept()
        elif choice == "6":
            handle_compare()
        elif choice == "7":
            show_about()
        elif choice == "0":
            running = False
            print("\n  Thank you for exploring Wirz. Goodbye!")
            print("=" * 60)
        else:
            print("  Invalid choice. Please enter a number 0-7.")


# Entry point - sequencing starts here
if __name__ == "__main__":
    main()
