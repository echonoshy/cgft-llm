from transformers import AutoTokenizer
from vllm import LLM, SamplingParams


def demo1():

    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]
    # Create a sampling params object.
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

    # Create an LLM.
    model_path = "/root/autodl-tmp/models/qwen2-1.5b"
    # model_path = "/root/autodl-tmp/models/glm-4-9b-chat"
    
    llm = LLM(model=model_path,
          trust_remote_code=True,
          tensor_parallel_size=2)

    outputs = llm.generate(prompts, sampling_params)
    # Print the outputs.
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")


def demo2():

    # 如果遇见 OOM 现象，建议减少max_model_len，或者增加tp_size
    max_model_len, tp_size = 32768, 2
    model = "/root/autodl-tmp/models/glm-4-9b-chat"
    prompt = [{"role": "user", "content": "你好"}]

    tokenizer = AutoTokenizer.from_pretrained(model, trust_remote_code=True) 
    
    llm = LLM(
        model=model,
        tensor_parallel_size=tp_size,
        max_model_len=max_model_len,
        trust_remote_code=True,
        enforce_eager=True,
    )
    stop_token_ids = [151329, 151336, 151338]
    sampling_params = SamplingParams(temperature=0.95, max_tokens=1024, stop_token_ids=stop_token_ids)

    inputs = tokenizer.apply_chat_template(prompt, tokenize=False, add_generation_prompt=True)
    outputs = llm.generate(prompts=inputs, sampling_params=sampling_params)

    print(outputs[0].outputs[0].text)


if __name__ == "__main__":
    
    demo1()
    # demo2()