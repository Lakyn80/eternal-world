import type { DemoImage } from '../demo';

interface Props {
  id: string;
  placeholder: string;
  className?: string;
  image?: DemoImage;
}

/** Drag-and-drop image placeholder. Wire this up to real upload/asset logic. */
export default function ImageSlot({ id, placeholder, className = '', image }: Props) {
  const onDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    // TODO: handle e.dataTransfer.files[0] upload
  };

  if (image) {
    return (
      <div id={id} className={`overflow-hidden rounded-2xl bg-black/20 ${className}`}>
        <img
          alt={image.alt}
          className="h-full w-full object-cover"
          decoding="async"
          loading="lazy"
          src={image.src}
          style={{ objectPosition: image.objectPosition ?? 'center' }}
        />
      </div>
    );
  }

  return (
    <div
      id={id}
      onDragOver={(e) => e.preventDefault()}
      onDrop={onDrop}
      className={`flex items-center justify-center text-center text-xs font-mono text-fg/40 bg-white/[0.03] border border-dashed border-white/15 rounded-2xl cursor-pointer select-none ${className}`}
      style={{
        backgroundImage:
          'repeating-linear-gradient(135deg, rgba(255,255,255,0.02) 0 10px, rgba(255,255,255,0.05) 10px 20px)'
      }}
    >
      {placeholder}
    </div>
  );
}
