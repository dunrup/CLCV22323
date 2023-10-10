Data normalization is a process or set of standards by which stored information is made consistent. Normalized data is necessary for analysts, as they require logical and consistent data storage in order to perform analysis on a dataset.

The First Normal Form has three requirements:
    1. All rows must be unique
    2. Each cell must contain a single value
    3. Each value must be non divisible

    1 ensures that each row can be referenced by one index. Each row corresponds to one entry with different aspects/information stored across the row in different columns.

    2 ensures that each cell has one data point. Thinking of analytics as a series of queries or questions, this ensures that each "question" one asks of a data set will return one "answer."

    3 ensures that each piece and different type of information is in separate columns within a row.

The Second Normal Form adds to the First Normal Form one additional requirement, no partial dependencies. All non-prime attributes are fully dependent on the candidate key. The Third Normal Form adds to Second the requirement that there is no transitive dependency. All fields must be determinably only by the primary/composite key. In other words, the index must be the value on which everything else depends. 

Both second and third normal forms seek to cut out interdependencies between different data types. This makes analysis more comprehensible and less prone to error.