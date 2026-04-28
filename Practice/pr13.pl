pack([],_,[]).
pack([box(Name,Size)|Rest],Cap,[Name|Arr]):-
    Size =< Cap,
    NewCap is Cap - Size,
    pack(Rest,NewCap,Arr).

pack([box(_,_)|Rest],Cap,Arr):-
    pack(Rest,Cap,Arr).