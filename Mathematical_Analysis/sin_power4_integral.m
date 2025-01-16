% Compute integral of sin^4(x)
xmin = 0;
xmax = 2*pi;
f = @myIntegrand;
a = integral(f,xmin,xmax)

function y = myIntegrand(x)
    y = sin(x).^4;
end

fplot(@myIntegrand) % Plot sin^4(x)
y = myIntegrand(x)

