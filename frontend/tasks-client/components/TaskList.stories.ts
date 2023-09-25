import type { Meta, StoryObj } from "@storybook/react";

import { TaskList } from "./TaskList";

const meta: Meta<typeof TaskList> = {
  component: TaskList,
  tags: ['autodocs'],
};

export default meta;
type Story = StoryObj<typeof TaskList>;

export const taskList: Story = {
  args: {
    tasks: [
      {
        id: "0",
        name: "Wash Dishes",
        completed: null,
      },
      {
        id: "1",
        name: "Feed Fishes",
        completed: new Date("2023-09-13T12:14:15Z"),
      },
      {
        id: "2",
        name: "Profit",
        completed: null,
      },
    ],
  },
};
