# # Hybrid & Hierarchical Inheritance... 



# # *** Hybrid Inheritance... 



# Hybrid inheritance is a combination of multiple inheritance and single inheritance in OOPs. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes intoo a single derived class, and single inheritance is used to inherit the properties of the derived class into a sub-derived class... 

# In python, hybrid inheritance can be implemented by creating a class hierarchy, in which a base class in inherited by multiple derived classes and one of the derived classes in further inherited by a sub-derived class... 




# # Syntax...


# class BaseClass:
#     pass

# class Derived_1(BaseClass):
#     pass

# class Derived_2(BaseClass):
#     pass

# class Derived_3(Derived_1, Derived_2):
#     pass









# # *** Hierarchical Inheritance... 



# Hierarchical Inheritance is a type of inheritance on OOPs where multiple subclasses inherit from a single base class. In other words, a single base class acts as a parent class for multiple subclasses. This is a way of established relationships between in a hierarchical manner...




# # Syntax... 



# class BaseClass:
#     pass

# class D_1(BaseClass):
#     pass

# class D_2(BaseClass):
#     pass

# class H_1(D_1):
#     pass

# class H_2(D_1):
#     pass

# class H_3(D_2):
#     pass

# class H_4(D_2):
#     pass

# class F_1(H_1):
#     pass

# class F_2(H_1):
#     pass

# class F_3(H_2):
#     pass

# class F_4(H_2):
#     pass