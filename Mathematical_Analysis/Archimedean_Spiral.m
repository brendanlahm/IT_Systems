% Archimedean Spiral

r = 10; % radius
inc = 10; % incerement per revolution
n = r/inc; % number of revolutions

i = linspace(0,n,1000); % create evenly spaced points between 0 & n
x = (inc*i).*cos(2*pi*i); % x coordinates
y = (inc*i).*sin(2*pi*i); % y coordinates

plot(x,y)
[x(end) y(end)]








