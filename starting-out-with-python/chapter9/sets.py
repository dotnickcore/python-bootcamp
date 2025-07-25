"""
    In this section, you will look at Program 9-3, which demonstrates various set operations.
    The program creates two sets: one that holds the names of students on the baseball team,
    and another that holds the names of students on the basketball team. The program then
    performs the following operations:
        
    • It finds the intersection of the sets to display the names of students who play both sports.
    • It finds the union of the sets to display the names of students who play either sport.
    • It finds the difference of the baseball and basketball sets to display the names of students who play baseball but not basketball.
    • It finds the difference of the basketball and baseball (basketball - baseball) sets to display the names of students who play basketball but not baseball. 
      It also finds the difference of the baseball and basketball (baseball - basketball) sets to display the names of students who play baseball but not basketball.
    • It finds the symmetric difference of the basketball and baseball sets to display the
    names of students who play one sport but not both.  
"""

# This program demonstrates various set operations.
baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

# Display members of the baseball set.
print('The following students are on the baseball team:')
for name in baseball:
    print(name)

# Display members of the basketball set.
print()
print('The following students are on the basketball team:')
for name in basketball:
    print(name)

# Demonstrate intersection
print()
print('The following students play both baseball and basketball:')
for name in baseball.intersection(basketball):
    print(name)

# Demonstrate union
print()
print('The following students play either baseball or basketball:')
for name in baseball.union(basketball):
    print(name)

# Demonstrate difference of baseball and basketball
print()
print('The following students play baseball, but not basketball:')
for name in baseball.difference(basketball):
    print(name)

# Demonstrate difference of basketball and baseball
print()
print('The following students play basketball, but not baseball:')
for name in basketball.difference(baseball):
    print(name)

# Demonstrate symmetric difference
print()
print('The following students play one sport, but not both:')
for name in baseball.symmetric_difference(basketball):
    print(name)