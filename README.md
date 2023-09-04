What is a language model?

#A language model allows machines to understand, generate, and analyze human language. Language models determine word probability by analyzing given text data. They will interpret this data by feeding it through an algorithm (set of rules) that establishes rules for context in natural language. Then, the model applies these rules in language tasks to predict or produce new sentences.

How does it work?

#It must learn by finding patterns. It disects a document and goes through a sequence of words one by one to store the probability of the last word occuring given the words before it. Then, it finds the "best" word (word with the greatest probabilty to occur after a squence of words) and identifies it as the best match for autofill given the initial words. 

How to empower a computer to behave like a language model?

#We write computer programs either based on statsitic or non-statistic methods to detect, store patterns found based on the given input sample data a.k.a. training data that can be used immitate auto fill sequence of words based on proceeding words.

How to evaluate capability of a given language model?
 
#some metrics could be - Check its content generation out of trained dataset context, How good the content generation is grammatically correct, Fluency close to human language etc.