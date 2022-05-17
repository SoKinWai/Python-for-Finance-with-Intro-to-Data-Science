#Student Name: Jianwei Su
#Date: 05/11/2022
#5.2.2



from functools import wraps





#Create a decorator that memoize’s the result of a function.
def memoize(f): #memoize function

    #Note that memoizing should happen on a per-parameter basis
    # This cache dict is to store every result
    cache_dict = {}

    #Nesting function
    @wraps(f) # Decorator that decorates the wrapped function to retain the representation of the function
    def wrapped(*args, **kwargs):  # Take all keyword and non-keyword parameters

        #Set the cache key
        cache_key=str(args)+str(kwargs)

        if cache_key not in cache_dict:
            cache_dict[cache_key] = f(*args, **kwargs)
        return cache_dict[cache_key]

    return wrapped