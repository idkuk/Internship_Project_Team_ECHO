# Prompt Injection Defense Tool v1.0
# Developed for Academic Research Paper

import re

class PromptInjectionDefenseTool:
    def __init__(self):
        # Define suspicious keywords and patterns
        self.suspicious_keywords = [
            "ignore", "override", "bypass", "forget",
            "disable safety", "act as", "simulate", "impersonate",
            "pretend to be", "neglect", "discard", "rewrite"
        ]

    def banner(self):
        print("="*50)
        print("   🛡️  Prompt Injection Defense Tool v1.0 🛡️")
        print("="*50)

    def show_menu(self):
        print("\nSelect an Option:")
        print("1. Check a single input")
        print("2. Check multiple inputs (bulk mode)")
        print("3. Exit")

    def check_input(self, user_input):
        found_threats = []
        input_lower = user_input.lower()
        for keyword in self.suspicious_keywords:
            if keyword in input_lower:
                found_threats.append(keyword)
        return found_threats

    def run_single_check(self):
        user_prompt = input("\nEnter the user prompt: ")
        threats = self.check_input(user_prompt)
        if threats:
            print(f"⚠️  Warning: Potential Prompt Injection Detected!")
            print(f"Threat Keywords Found: {threats}")
        else:
            print("✅ No suspicious patterns detected.")

    def run_bulk_check(self):
        num_inputs = int(input("\nHow many prompts would you like to check? "))
        flagged_prompts = []

        for i in range(1, num_inputs + 1):
            prompt = input(f"Enter Prompt {i}: ")
            threats = self.check_input(prompt)
            if threats:
                flagged_prompts.append((prompt, threats))

        if flagged_prompts:
            print("\n⚠️  Summary of Detected Threats:")
            for idx, (prompt, threats) in enumerate(flagged_prompts, start=1):
                print(f"\n{idx}. Prompt: {prompt}")
                print(f"   Detected Threats: {threats}")
        else:
            print("\n✅ All prompts are clean. No issues found.")

    def start(self):
        self.banner()
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-3): ")

            if choice == '1':
                self.run_single_check()
            elif choice == '2':
                self.run_bulk_check()
            elif choice == '3':
                print("\nThank you for using the Prompt Injection Defense Tool. Stay Safe! 🛡️")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tool = PromptInjectionDefenseTool()
    tool.start()
