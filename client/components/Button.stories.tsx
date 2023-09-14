import type { Meta, StoryObj } from "@storybook/react";

import { Button } from "./Button";

const meta: Meta<typeof Button> = {
  component: Button,
  argTypes: {
    variant: {
      options: ["primary", "default"],
      control: { type: "radio" },
    },
  },
};

export default meta;
type Story = StoryObj<typeof Button>;

export const button: Story = {
  args: {
    children: "Hello, World!",
    variant: "primary",
    disabled: false,
  },
};
