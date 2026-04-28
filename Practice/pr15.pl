% Positions
position(door).
position(window).
position(middle).

% Goal
goal(state(_, _, _, yes)).

% Walk
move(state(From, Box, floor, Banana),
     state(To, Box, floor, Banana),
     walk(To)) :-
    position(To),
    From \= To.

% Push box
move(state(Pos, Pos, floor, Banana),
     state(To, To, floor, Banana),
     push_box(Pos, To)) :-
    position(To),
    Pos \= To.

% Climb
move(state(Pos, Pos, floor, Banana),
     state(Pos, Pos, onbox, Banana),
     climb).

% Grab banana
move(state(middle, middle, onbox, no),
     state(middle, middle, onbox, yes),
     grab_banana).

% Solve
solve(State, _, []) :- goal(State).
solve(State, Visited, [Action|Actions]) :-
    move(State, NewState, Action),
    \+ member(NewState, Visited),
    solve(NewState, [NewState|Visited], Actions).

% Main
main :-
    Initial = state(door, window, floor, no),
    solve(Initial, [Initial], Plan),
    write('Solution:'), nl,
    maplist(writeln, Plan).