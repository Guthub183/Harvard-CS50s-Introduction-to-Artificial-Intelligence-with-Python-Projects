# Analysis

## Layer 10, Head 11: [MASK] Token Focus (Context Gathering)

This attention head is characterized by a very strong focus on the `[MASK]` token. For almost every token in the input sentence, the highest attention weight is directed toward the `[MASK]` token.

**Intuition:** In BERT's masked language modeling task, the model must predict the token at the `[MASK]` position. This head acts as a contextual aggregator, allowing other words in the sentence to focus their attention on the masked slot to help compile and route the necessary context (e.g., verbs, adjectives) to resolve the missing word.

Example Sentences:
- "I threw a small rock and it fell in the [MASK]."
- "The turtle moved slowly across the [MASK]."

## Layer 12, Head 9: Relative Positional Focus (Diagonal Neighborhood Attention)

This head exhibits a clean, prominent diagonal pattern along the attention matrix. Each token distributes its attention primarily to its immediate neighbors (the words directly preceding or following it).

**Intuition:** This head captures local syntactic and positional context. In natural language, a word's immediate neighbors carry the most direct relationships (such as adjectives modifying adjacent nouns or prepositions relating to neighboring nouns). This head helps compile local phrase-level representations.

Example Sentences:
- "We wrote a [MASK] about our journey."
- "The book was lying on the [MASK]."
