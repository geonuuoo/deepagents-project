from deepagents import create_deep_agent

summary_agent = {
    "name": "summary-agent",
    "description": "학습 자료를 요약하는 에이전트",
    "system_prompt": """
반드시 한국어로만 답변하라.
주어진 학습 내용을 핵심 개념 위주로 3~4개의 bullet로 요약하라.
[요약] 섹션 내용만 생성하라.
다른 섹션은 만들지 마라.
중복 표현 금지.
"""
}

todo_agent = {
    "name": "todo-agent",
    "description": "해야 할 일을 생성하는 에이전트",
    "system_prompt": """
반드시 한국어로만 답변하라.
입력 내용을 바탕으로 학습 TODO를 3~4개 생성하라.
[TODO] 섹션 내용만 생성하라.
다른 섹션은 만들지 마라.
중복 표현 금지.
"""
}

schedule_agent = {
    "name": "schedule-agent",
    "description": "학습 일정을 추천하는 에이전트",
    "system_prompt": """
반드시 한국어로만 답변하라.
입력 내용을 바탕으로 3일 학습 일정을 추천하라.
[추천 일정] 섹션 내용만 생성하라.
다른 섹션은 만들지 마라.
중복 표현 금지.
"""
}

agent = create_deep_agent(
    model="openrouter:openrouter/auto",
    subagents=[summary_agent, todo_agent, schedule_agent],
    system_prompt="""
너는 학생/대학생을 위한 학습 일정 관리 AI 에이전트다.

반드시 아래 규칙을 지켜라.
1. 한국어로만 답한다.
2. 최종 답변은 단 한 번만 출력한다.
3. 형식은 아래와 정확히 같아야 한다.
4. 같은 내용을 반복하지 마라.
5. 불필요한 설명은 쓰지 마라.

최종 출력 형식:

[요약]
- ...
- ...

[TODO]
- ...
- ...

[추천 일정]
- 1일차: ...
- 2일차: ...
- 3일차: ...

작업 순서:
1. summary-agent로 요약
2. todo-agent로 TODO 생성
3. schedule-agent로 일정 추천
4. 마지막에 하나의 통합된 최종 답변만 출력
"""
)

if __name__ == "__main__":
    print("🚀 DeepAgents 실행 중...\n")

    user_input = input("학습할 내용을 입력하세요: ").strip()

    if not user_input:
        print("입력이 비어 있습니다. 다시 실행해서 학습 내용을 입력하세요.")
        raise SystemExit

    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    })

    final_text = result["messages"][-1].content.strip()

    second_summary = final_text.find("[요약]", final_text.find("[요약]") + 1)
    if second_summary != -1:
        final_text = final_text[:second_summary].strip()

    print("\n📌 결과 출력\n")
    print(final_text)