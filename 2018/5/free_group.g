input := InputTextFile("input.txt");
data := ReadLine(input);
RemoveCharacters(data, " \n\t\r");

f := FreeGroup("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z");

n := Length(data);

outcome := function (data)
    local result,i,n,rc,lc;
    n := Length(data);
    result := f.a*f.a^-1;
    for i in [1 .. n] do
        rc := data{[i .. i]};
        lc := LowercaseString(rc);
        if rc = lc then
            result := result*EvalString(Concatenation("f.",lc));
        else
            result := result*EvalString(Concatenation(Concatenation("f.",lc),"^-1"));
        fi;
    od;
    return result;
end;

