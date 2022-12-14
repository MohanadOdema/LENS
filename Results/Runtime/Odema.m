a = [24.45
12.2
10.66
13.65
4.94
6.46
12.94
11.64
13.42
5.6
5.35
17.28
13.69
12.18
8.21
9.94
12.32
8.39
13.48
9.77
8.67
12.9
14.04
24.76
11.21
10.98
11.13
13.03
13.92
4.29
7.93
7.8
11.75
6.36
20.16
18.11
4.53
9.19
7.69
11.8
6.32
7.52
17.32
5.32
16.1
10.33
8.41
30.63
18.83
5.76
16.67
12.55
15.37
11.65
10.8
13.1
10.52
10.36
10.29
7.27
10.51
10.65
11.56
4.69
5.95
15.33
8.99
12.74
11.14
11.15
14.32
9.24
11.19
12.48
12.31
12.14
12.94
12.08
8.39
13.78
12.27
4.22
13.21
7.93
7.3
25.88
15.47
4.71
11.79
10.37
16.59
26.91
28.66
9.03
12.36
30.3
26.26
28.48
28.23
10.41
26.42
22.83
18.38
21.44
26.48
24.54
9.06
9.6
8.56
17.62
17.95
14.97
15.34
17.58
16.33
28.95
15.25
14.58
15.29
18.81
4.65
5.86
5.6
5.77
15.42
13.29
5.64
7.67
9.02
8.65
8.91
16.27
21.28
17.33
5.96
14.36
6.56
13.02
3.79
4.79
13.52
12.44
13.88
4.05
14.54
17.71
4.5
8.47
7.76
8.67
8.59
7.63
8.69
8.3
7.71
10.74
11.93
15.34
16.81
14.22
19.03
17.04
16.44
];
a1 = resample(a,500,163);
Epart_t = 0;
Lpart_t_arr = [];
Lcloud_t = 0;
Eedge_t_arr = [];
counter = 0;
counter_arr = [];

for i = 1:500
    if a1(i) < 55
        Lcloud_t = Lcloud_t + 1204 / a1(i);
    end
    if a1(i) < 55
        Epart_t = Epart_t + (46 + 150.5/ a1(i));
    end
    if a1(i) < 22
        counter = counter + (46 + 150.5/ a1(i));
    else
        counter = counter + 1204 / a1(i);
    end
    Lpart_t_arr(i) = Epart_t;
    Eedge_t_arr(i) = Lcloud_t;
    counter_arr(i) = counter;
end

figure,plot(a1), hold on ,
plot(Eedge_t_arr * 0.001),
hold on,plot(Lpart_t_arr * 0.001),
hold on ,plot(counter_arr * 0.001),
legend('MBPS','All-edge','All-Par','Dynamic')
%% Energy
% for i = 1:500
%     if a1(i) < 55
%         Eedge_t = Eedge_t + Eedge;
%     end
%     if a1(i) < 55
%         Epart_t = Epart_t + (484 * a1(i) + 1288) * (18816*8)/(a1(i)*1000000);
%     end
%     if a1(i) < 6.77
%         counter = counter + Eedge;
%     else
%         counter = counter + (484 * a1(i) + 1288) * (18816*8)/(a1(i)*1000000);
%     end
%     Epart_t_arr(i) = Epart_t;
%     Eedge_t_arr(i) = Eedge_t;
%     counter_arr(i) = counter;
% end

% figure,plot(a1), hold on ,
% plot(Eedge_t_arr * 0.001),
% hold on,plot(Epart_t_arr * 0.001),
% hold on ,plot(counter_arr * 0.001),
% legend('MBPS','All-edge','All-Par','Dynamic')