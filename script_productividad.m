clear all
Yxs=0.5;
Si=10;
um=0.2;
Ks=1;
a=0.7;
b=1.5;
Dr=linspace(0.01,0.279,20);
D=linspace(0.01,0.18,20);
den_a_b=(1+a)-a*b;

%without recycle
y=D.*Yxs.*(Si-(D.*Ks./(um-D)));
plot(D,y,'v-r')
hold on


%with recycle
ur=Dr.*den_a_b;
Sr=ur.*Ks./(um-ur);
yr=Dr.*(Si-Sr).*Yxs./den_a_b;
plot(Dr,yr, '*-b')
hold off

grid on
