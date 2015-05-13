%Variables assignment
Var = 24. % Note the first letter capital and termination char .
%Pattern Matching
Person = {person, {name, "Agent Smith"}, {profession, "killing programs}}.

%pattern match
{person, {name, Name}, {profession, Profession}} = Person.

Name.


%Case statement for control flow
Animal = "dog".
case Animal of
    "dog"   -> underdog;
    "cat"   -> thundercat
end.

case Animal of
    "elephant" -> dumbo;
    _ -> "not elephant"
end.

if
    ProgramsTerminated > 0 ->
        success;
    ProgramsTerminated < 0 ->
        error;
    true -> zero    % for default values/else..if is a function here.
end.



% Anonymous functions
Negate = fun(I) -> -I end.

Numbers = [1,2,3,4].
lists:foreach(fun(Number) -> io:format("~p~n", [Number]) end, Numbers).

lists:map(fun(X) -> X +1 end, Numbers).

Small = fun(X) -> X < 3 end.


lists:filter(Small, Numbers).

lists:all(Small, [0,1,2]).
lists:all(Small, Numbers).

lists:any(Small, [0,1,2,3]).
lists:any(Small, [3,4,5]).

lists:takewhile(Small, Numbers).
lists:dropwhile(Small, Numbers).

lists:foldl(fun(X, Sum) -> X + Sum end, 0, Numbers).

Adder = fun(ListItem, SumSoFar) -> ListItem + SumSoFar end.





