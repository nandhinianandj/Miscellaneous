-module(double).
-export([double_all/1]).

dobule_all([]) -> [];
double_all([First|Rest]) -> [First + First|double_all(Rest)].
