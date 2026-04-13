#  DeepAgents 기반 학습 일정 관리 시스템

##  프로젝트 개요

본 프로젝트는 DeepAgents를 활용하여 학습 내용을 자동으로 분석하고,
요약 → TODO 생성 → 학습 일정 추천까지 수행하는
**Multi-Agent 기반 학습 도우미 시스템**을 구현한 것이다.

단일 AI 모델이 아닌 여러 에이전트가 협업하는 구조를 통해
더 체계적인 결과를 생성하는 것을 목표로 한다.

---

##  에이전트 목표

* 학습 내용을 자동으로 요약
* 학습해야 할 TODO 생성
* 효율적인 학습 일정 추천
* Multi-Agent 협업 구조 구현

---

##  시스템 구조

본 시스템은 총 **4개의 에이전트**로 구성된다.

### 🔹 Main Agent (1개)

* 전체 흐름 제어
* 서브 에이전트 호출
* 최종 결과 통합

### 🔹 Sub Agents (3개)

1. **Summary Agent**

   * 입력된 내용을 요약

2. **TODO Agent**

   * 요약된 내용을 기반으로 할 일 생성

3. **Schedule Agent**

   * TODO를 기반으로 학습 일정 추천

---

##  동작 원리

```
사용자 입력
   ↓
Main Agent
   ↓
Summary Agent
   ↓
TODO Agent
   ↓
Schedule Agent
   ↓
최종 결과 출력
```

---

##  실행 방법

### 1. 가상환경 활성화

```
.venv\Scripts\activate
```

### 2. 실행

```
python app.py
```

### 3. 입력

```
학습할 내용을 입력하세요:
```

---

## 📊 실행 결과 예시

### 입력

```
운영체제 시험 범위: 프로세스, 스레드, CPU 스케줄링, 교착상태
```

---

### 출력

#### [요약]

* 프로세스: 실행 중인 프로그램
* 스레드: 프로세스 내 실행 단위
* CPU 스케줄링: CPU 자원 할당 방식
* 교착상태: 자원 대기로 인한 무한 대기 상태
<img width="1355" height="661" alt="image" src="https://github.com/user-attachments/assets/7990f730-cebe-492b-bbbd-5c61e94a0a31" />

<img width="865" height="401" alt="image" src="https://github.com/user-attachments/assets/5382bafa-16fe-4664-8964-a92417a2b864" />

---

#### [TODO]

* 프로세스와 스레드 개념 학습
* CPU 스케줄링 알고리즘 이해
* 교착상태 조건 및 해결 방법 학습
* 문제 풀이 및 복습

---

#### [추천 일정]

* 1일차: 프로세스와 스레드 학습
* 2일차: CPU 스케줄링 학습
* 3일차: 교착상태 및 전체 복습

---

##  주요 코드

```python
agent = create_deep_agent(
    model="openrouter:openrouter/auto",
    subagents=[summary_agent, todo_agent, schedule_agent],
)
```

---

##  특징

* DeepAgents 기반 Multi-Agent 구조
* 역할 분리 (요약 / TODO / 일정)
* 단계별 논리 처리 (Multi-step reasoning)
* 사용자 입력 기반 동적 실행

---

##  결론

본 프로젝트는 DeepAgents를 활용하여
여러 에이전트가 협업하는 구조를 구현하였다.

이를 통해 단일 모델보다 더 구조적이고 확장 가능한
AI 시스템을 설계할 수 있음을 확인하였다.
