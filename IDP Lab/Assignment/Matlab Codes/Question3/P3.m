die = [1/6 1/6 1/6 1/6 1/6 1/6];
average = 1;
N=2;
for c = 1:N
    average = conv(average,die);
end

xaxis = [0:length(average)-1] + N ;
xaxis = xaxis/N;
figure();
set(gca,'Linewidth',1.6);
set(gca,'FontSize',12);
bar(xaxis,average);
axis([1 6 -inf inf]);
title('DistributionoftheEmpiricalAverage,N=2');
print('-depsc','EmpAverage2.eps');