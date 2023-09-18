# **What is a language model?**

A language model enables machines to comprehend, generate, and analyze human language. These models ascertain word probabilities by examining provided text data. They process this data through an algorithm, which defines contextual rules in natural language. Subsequently, these rules are applied in language-related tasks to anticipate or generate new sentences.

# **How does it work?**

It must learn by finding patterns. It disects a document and goes through a sequence of words one by one to store the probability of the last word occuring given the words that come before it. Then, it finds the "best" word (word with the greatest probabilty to occur after a squence of words) and identifies it as the best match for autofill given the initial words. 

# **How to empower a computer to behave like a language model:**

We write computer programs either based on statsitic or non-statistic methods to detect, store patterns found based on the given input sample data a.k.a. training data that can be used immitate autofill a sequence of words based on proceeding words.

# **How to evaluate the capabilities of a given language model:**
 
Some metrics could be: check its content generation out of a trained dataset context, check how good the content generation is based on criteria (for example how grammatically correct it is), how close its fluency is to human language, etc.
