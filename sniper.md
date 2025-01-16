区间核心模型 (interval core model)：通过模拟处理器核心之间的“失效事件 (miss events)”之间的时间间隔，而不是逐周期地进行详细建模，从而加快了模拟速度。它在提高模拟速度的同时，允许在速度和准确性之间进行权衡。

Graphite 仿真基础设施： Graphite 是一个面向分布式共享内存 (DSM) 的仿真平台，支持大规模多核架构的性能研究。
分布式共享内存 (Distributed Shared Memory, DSM)用于在分布式系统中模拟一个全局共享的内存空间。

docker: `make run`
sniper: `cd sniper/test/fft; make run`
`./run-sniper -- /bin/ls -d <out-dir>`

performance model = ROI内需要仔细仿真的内容

analytical model、numerical model 和 empirical model 为模型分类
