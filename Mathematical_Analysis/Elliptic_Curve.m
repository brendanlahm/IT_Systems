% Elliptic Curve
n = 1000;
x = -2:1/n:2;
y = sqrt(x.^3 + 2*x + 10);
iy = find(y~=real(y));
y(iy) = nan;
y1 = (1 + y)/2;
y2 = (1 - y)/2;
plot(x,y1,'r',x,y2,'r') % Plot elliptic curve



