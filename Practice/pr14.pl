% Length of list
list_length([], 0).
list_length([_|T], N) :-     % _ ignores head value
    list_length(T, N1),
    N is N1 + 1.

% Sum of list
list_sum([], 0).
list_sum([H|T], S) :-
    list_sum(T, S1),
    S is S1 + H.

% Maximum of list
list_max([X], X).            % single element
list_max([H|T], Max) :-
    list_max(T, TMax),
    Max is max(H, TMax).

% Reverse a list
list_rev([], []).
list_rev([H|T], R) :-
    list_rev(T, RT),
    append(RT, [H], R).

% Member check
my_member(X, [X|_]).         % X is the head
my_member(X, [_|T]) :-
    my_member(X, T).         % X is in tail

