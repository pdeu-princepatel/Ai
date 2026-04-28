parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).

grandparent(X,Z) :- 
    parent(X,Y),
    parent(Y,Z).

ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :-
    parent(X,Z),
    ancestor(Z,Y).

sibling(X,Y) :-
    parent(P,X),
    parent(P,Y),
    X =\= Y.

area(R,A) :- A is 3.14 * R * R .

first([H|_],H).
rest([_|T],T).
