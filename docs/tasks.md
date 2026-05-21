# Task decomposition of Reproducing Research and scoring reproducibility

This is an effort to decompose the main tasks of a reproducibility research paired with the overall goal of our research which is automated reproducibility. It adds the evaluation of reproducibility, essentially a measurement of reproducibility for research papers. To avoid confusion between the components of a paper and reproducibility experiemnt the components related with reproducibility experiment are marked with **RE**.

## Main tasks

We decompose the main tasks into the following:

1. **Understand** the research
2. **Plan** the execution of the reproducibility experiment
3. **Execute** the reproducibility experiment
4. **Analyze** the resilt from the reproducibility experiment
5. **Evaluate** the analysis and conclude reproducibility

it is also possible to add a 6th step

6. **Explain** the reproducibility evaluation and score

These tasks has their own sub tasks. The process is described in a sequence diagrams below.

### 1. Subtasks Understand

```mermaid
sequenceDiagram
box lime INPUTS
participant P as Paper
end
box Cyan UNDERSTAND
participant A1 as Research Question & Goal
participant A2 as Hypothesis
participant A3 as Experiment Plan
participant A4 as Experiment Result
participant A5 as Research Conclusions
end

P->>A1: Extracting information from paper
P->>A2:
P->>A3:
P->>A4:
P->>A5:

box lime OUTPUTS
participant K as Extracted Knowledge
end

A1->>K: Outputs structured knowledge with relations between RQ, Hypothesis, Experiment, Results, and Conclusions
A2->>K:
A3->>K:
A4->>K:
A5->>K:
```

### 2. Subtasks Plan

```mermaid
sequenceDiagram
box lime INPUTS
participant EK as Extracted Knowledge
participant P as Paper
end
box yellow PLAN EXECUTION
participant B1 as Find Resources Avilable
participant B2 as Create Experiment Plan
participant B3 as Fetch Resources
end

B1->>P: Evaluate Resources (Code and data)
B1->>B2:
B2->>EK: Get experiment and hypothesis information
B2-->>B3: Fetch necessary <br/> external resources if needed
B2->>PL: Create and save experiment plan

box lime OUTPUTS
participant PL as Plan
end
```

### 3. Subtasks Execute

```mermaid
sequenceDiagram
box lime INPUTS
participant PL as Plan
end
box pink EXECUTE
participant C1 as Gather / build data and code
participant C2 as Create Execution Environment
participant C3 as Produce RE Result
end
box lime OUTPUTS
participant R as RE Results
end
PL->>C1: Plan and resources
C1-->>C1: Possibly build code and data

loop Until Resolved
    C1->>C2: Provide execution stack
    C2->>C2: Build environment for code
    C2-->>C1: Possibly request code changes
    C2->>C3: Prompt execution
    C3->>C3: Build results
    C3-->>C2: Possible errors
    C3-->>C1: Possible errors
    PL->>C3: Sanity check results with plan
    C3-->>C1:Possible changes from <br/> sanity check
end

C3->>R: Return RE Results

```

### 4. Subtasks Analyse

```mermaid
sequenceDiagram
box lime INPUTS
    participant PL as Plan
    participant R as Results
end
box rgb(255,128,1) ANALYSE
    participant GM as Generate Metrics
    participant PT as Perform Tests
    participant CR as Conclude Tests
end
box lime OUTPUTS
    participant REC as RE Conclusions
end

PL->>GM: Provide evaluation strategy from<br/> RE experiment plan
R->>GM: Pass RE Results
GM->>GM: Generate metrics
GM->>PT: Pass metrics
PT->>PT: Generate test results RE
PT->>CR: Pass test results RE
PL->>CR: Pass hypothesis of RE experiments run in Execution phase
CR->>CR: Make conclusions based on <br/> passed hypothesis
CR->>REC: Pass RE Conclusions
```

### 5. Subtasks Evaluate Reproducbility

```mermaid
sequenceDiagram
box lime INPUTS
    participant EK as Extracted Knowledge
    participant REC as RE Conclusions (REC)

end
box rgb(255,100,255) Evaluate Reproducibility
    participant CC as Compare Conclusions
    participant ARS as Assign Reproducibility (score)
end
box lime OUTPUTS
    participant RE as Reproducibility Evaluation
end

EK->>CC: Pass Conclusions from original Paper
REC->>CC: Pass REC's

CC->>CC: Measure similarity of conclusions?
CC->>ARS: Pass comparisons
CC->>RE: Pass comparisons

ARS->> ARS: Generate reproducibility score
ARS->>RE: Pass scores
```

### 6. Subtask Explain Reproducibility Evaluation and Score

```mermaid
sequenceDiagram
box lightblue Input
    participant EK as Extracted Knowledge
    participant PL as Plan
    participant R as Results RE
    participant REC as RE Conclusions
    participant RE as Reproducibility Evaluation
end

box Summarised Reproducibility Research (RR)
    participant ER as Explain RR
end
EK-->>ER: Extracted information from the paper
PL-->>ER: Execution plan with available resources
R-->>ER: Results from the reproucivility experiments
REC-->>ER: Interpretations and conclusions from RE
RE-->>ER: Comparison of conlusions <br> from paper and RE <br> with reproducibility evaluations


```
