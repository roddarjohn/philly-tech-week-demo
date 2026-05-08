# Why pipelines?

- Enables multi model work
  - One model can review work of another model
  
- Introspect intermediate outputs
  - Critical to iterate (a la Unix pipes)
  
- Security: can lock tools / MCPs to specific steps
  - e.g. step 1 can research certain sites
  - step 2 can research all sites but can only be run once
  
- Context isolation
  - Each agent gets only the context it needs
  - Can result in higher quality focused work
  - Some tasks require large context windows, some require less

- Parallelism

- Composability
  - Many workflows may have similar components that you can reuse (example six)
  
Sample "production" example: example seven

RFPs are a simple example, you could also pipeline coding, design,
anything you use AI for.
  
https://tinyurl.com/philly-tech-week-crew-ai
