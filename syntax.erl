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
    true -> zero
end.




