% Bisection Search

function y = f(x)
    y = x^2-2;
    disp(y)
end

i = 0;
function [a,b] = bisection(i)

    a = 0.1;
    disp("f(a):")
    disp(f(a))
    b = 3;
    disp("f(b):")
    disp(f(b))
    c = (a+b)/2;
    disp("C:")
    disp(c)
    disp("f(c):")
    disp(f(c))
    tol = 0.01;
    maxit = 4;

    if f(a)*f(b) >= 0
        disp("Method Not Applicable")
        disp("f(a)*f(b) >= 0")
        disp(f(a).*f(b))
        return
    else
        disp("Method Applicable")
        disp("f(a)*f(b) < 0")
        disp(f(a).*f(b))
    end
    while i <= maxit
        if abs(f(c)) < tol | (b-a)/2 < tol
            disp("Solution")
            disp("Absolute Value of f(c):")
            disp(abs(f(c)))
            disp("b-a/2:")
            disp((b-a)/2)
            return
        end
        disp("f(c)*f(a):")
        disp(f(c)*f(a))
        if f(c)*f(a) >= 0
            a = c;
            disp("New a:")
            disp(a)
        else 
            b = c;
            disp("New b:")
            disp(b)
        end
        c = (a+b)/2;
        disp("New c:")
        disp(c)
        i = i+1;
    end
end

[a,b] = bisection(i)